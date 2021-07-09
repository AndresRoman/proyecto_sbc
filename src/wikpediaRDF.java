/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sbc;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.RDFNode;
import org.apache.jena.rdf.model.RDFWriterI;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.Statement;
import org.apache.jena.rdf.model.StmtIterator;
import org.apache.jena.riot.RDFWriter;
import org.apache.jena.sparql.vocabulary.FOAF;


/**
 *
 * @author Andres Roman
 */
public class wikpediaRDF {

    static String DataFilePath = "C:/Users/andre/Desktop/SBC/";
    
    static String concept = "concepts.csv";// sct:subject
    static String instance = "instances2.csv";// foaf:primaryTopicOf
    static String wikipage = "wikipages.csv";

    static String GenFilePath = "C:/Users/andre/Desktop/SBC/GeneralRDF.rdf";
    
    public static void main(String[] args) throws FileNotFoundException {

        List<concept> concepts = readConceptsFromCSV(DataFilePath + concept);
        List<instance> instances = readInstancesFromCSV(DataFilePath + instance);
        List<wikipage> wikipages = readWikipagesFromCSV(DataFilePath + wikipage);

        Model model = ModelFactory.createDefaultModel();
        File f = new File(GenFilePath);
        FileOutputStream os = new FileOutputStream(f);
        
       
        ////////////////////////////////////////////////////////////
        String data = "http://ky.utpl.edu.ec/wikipediaqa/data#";
        model.setNsPrefix("myonto", data);
        Model datamodel = ModelFactory.createDefaultModel();
        
        String skos = "http://www.w3.org/2004/02/skos/core";
        model.setNsPrefix("skos", skos);
        Model skosmodel = ModelFactory.createDefaultModel();
                
        String owl = "http://www.w3.org/2002/07/owl";
        model.setNsPrefix("owl", owl);
        Model owlmodel = ModelFactory.createDefaultModel();
        
        String dbo = "http://dbpedia.org/ontology/";
        model.setNsPrefix("dbo", dbo);
        Model dbomodel = ModelFactory.createDefaultModel();

        Resource  instancia = null, concepto = null, wikipediaPage = null;

        
        for (concept conce : concepts) {
            //System.out.println(conce);
            concepto = model.createResource(skos + conce.getPrefLabel());
        }
        
        for (instance insta : instances) {
            //System.out.println(insta);
            instancia = model.createResource(datamodel + insta.getDbResource())
                    .addProperty(datamodel.getProperty(data + "wikiPageModified"), insta.getWikiPageModified())
                    .addProperty(datamodel.getProperty(data + "maxOutDegree"), insta.getMaxOutDegree());

        }

        for (wikipage var : wikipages) {
            
            //System.out.println(var);
            wikipediaPage = model.createResource(owl + var.getWikipageUrl());

        }
        
        
        StmtIterator iter = model.listStatements();

        System.out.println("TRIPLES");
        while (iter.hasNext()) {
            Statement stmt = iter.nextStatement();  // get next statement
            Resource subject = stmt.getSubject();     // get the subject
            Property predicate = stmt.getPredicate();   // get the predicate
            RDFNode object = stmt.getObject();      // get the object

            System.out.print(subject.toString());
            System.out.print(" " + predicate.toString() + " ");
            if (object instanceof Resource) {
                System.out.print(object.toString());
            } else {
                // object is a literal
                System.out.print(" \"" + object.toString() + "\"");
            }

            System.out.println(" .");
        }
        // now write the model in XML form to a file

        System.out.println(
                "MODELO RDF------");
        model.write(System.out,
                "Turtle");

        // Save to a file
        RDFWriterI writer = model.getWriter("Turtle");

        writer.write(model, os, "");

        //Close models
        dbomodel.close();

        model.close();
    }

    private static List<concept> readConceptsFromCSV(String fileName) {
        List<concept> concepts = new ArrayList<>();
        Path pathToFile = Paths.get(fileName);

        try (BufferedReader br = Files.newBufferedReader(pathToFile)) {

            String line = br.readLine();

            while (line != null) {
                String[] attributes = line.split(";");
                concept concepto = createConcept(attributes);

                concepts.add(concepto);

                line = br.readLine();
            }

        } catch (IOException ioe) {
            ioe.printStackTrace();
        }

        return concepts;
    }

    private static List<instance> readInstancesFromCSV(String fileName) {
        List<instance> instances = new ArrayList<>();
        Path pathToFile = Paths.get(fileName);

        try (BufferedReader br = Files.newBufferedReader(pathToFile)) {

            String line = br.readLine();

            while (line != null) {

                String[] attributes = line.split(";");

                instance instance = createInstance(attributes);

                // adding person into ArrayList
                instances.add(instance);

                // read next line before looping
                // if end of file reached, line would be null
                line = br.readLine();
            }

        } catch (IOException ioe) {
            ioe.printStackTrace();
        }

        return instances;
    }

    private static List<wikipage> readWikipagesFromCSV(String fileName) {
        List<wikipage> wikipages = new ArrayList<>();
        Path pathToFile = Paths.get(fileName);

        try (BufferedReader br = Files.newBufferedReader(pathToFile)) {

            String line = br.readLine();

            while (line != null) {

                String[] attributes = line.split(";");

                wikipage wikipage = createWikipage(attributes);

                // adding person into ArrayList
                wikipages.add(wikipage);

                // read next line before looping
                // if end of file reached, line would be null
                line = br.readLine();
            }

        } catch (IOException ioe) {
            ioe.printStackTrace();
        }

        return wikipages;
    }

    
    private static concept createConcept(String[] metadata) {

        String prefLabel = metadata[0];

        return new concept(prefLabel);
    }

    private static instance createInstance(String[] metadata) {

        String dbResource = metadata[0];
        String wikiPageModified = metadata[1];
        String maxOutDegree = metadata[2];

        return new instance(dbResource, wikiPageModified, maxOutDegree);
    }

    private static wikipage createWikipage(String[] metadata) {

        String id = metadata[0];
        String wikipageUrl = metadata[1];

        return new wikipage(id, wikipageUrl);
    }
   
}


//Creación de clases
class concept {

    private String prefLabel;

    public concept(String prefLabel) {
        this.prefLabel = prefLabel;
    }


    public String getPrefLabel() {
        return prefLabel;
    }

    public void setPrefLabel(String prefLabel) {
        this.prefLabel = prefLabel;
    }
}

class subject{
    
}

class instance extends concept{
    
    private String dbResource;
    private String wikiPageModified;
    private String maxOutDegree;

    public instance(String dbResource, String wikiPageModified, String maxOutDegree) {
        super(dbResource);
        this.dbResource = dbResource;
        this.wikiPageModified = wikiPageModified;
        this.maxOutDegree = maxOutDegree;
    }

    


    public String getDbResource() {
        return dbResource;
    }

    public void setDbResource(String dbResource) {
        this.dbResource = dbResource;
    }

    public String getWikiPageModified() {
        return wikiPageModified;
    }

    public void setWikiPageModified(String wikiPageModified) {
        this.wikiPageModified = wikiPageModified;
    }

    public String getMaxOutDegree() {
        return maxOutDegree;
    }

    public void setMaxOutDegree(String maxOutDegree) {
        this.maxOutDegree = maxOutDegree;
    }
    
}

class wikipage {
    
    private String id;
    private String wikipageUrl;

    public wikipage(String id, String wikipageUrl) {
        this.id = id;
        this.wikipageUrl = wikipageUrl;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getWikipageUrl() {
        return wikipageUrl;
    }

    public void setWikipageUrl(String wikipageUrl) {
        this.wikipageUrl = wikipageUrl;
    }
    
    
}