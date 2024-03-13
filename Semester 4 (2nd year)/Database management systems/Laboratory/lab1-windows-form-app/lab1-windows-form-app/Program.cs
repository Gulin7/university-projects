using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;

namespace lab1_windows_form_app
{
    /*
     REQUIREMENTS
    - Create a Windows Form Application
    - Have a form that allows the user to manipulate the data in 2 tables that are 1:n
    - Functionalities:
        - display all records from the parent table
        - display all records from the child table for a specific parent record
        - add/remove/update child records for a specific parent record
    NotionDatabase:
    - parent table = areas
    - child table = projects ( for a specific area id be able to add/remove/update display 
    from projects table)
     */
    internal class Program
    {
        static void Main(string[] args)
        {
            // create a connection string ( to the database server(data source)
            // the database name(initial catalog)
            // and the security settings(integrated security)
            string connectionString =
                "Data Source=GT-LENOVO\\SQLEXPRESS;" +
                "Initial Catalog=NotionDatabase;" +
                "Integrated Security=True";
            // create a connection to the database
            SqlConnection connection = new SqlConnection(connectionString);
            // open the connection
            connection.Open();
            // SqlCommand - to display all from areas
            string selectAreas = "SELECT * FROM areas";
            SqlCommand command = new SqlCommand(selectAreas, connection);
            // SqlDataReader - to obtain the result of the select statement
            using(SqlDataReader reader = command.ExecuteReader())
            {
                while (reader.Read())
                {
                    Console.WriteLine("{0}, {1}, {2}, {3}", reader[0], reader[1], reader[2], reader[3]);
                }
            }  
            connection.Close();
            // SqlCommand - to display all from projects with given area_id
            string stringProjectsInArea
                = "SELECT * FROM projects WHERE area_id = @area_id";
            SqlCommand commandProjectsInArea = new SqlCommand(stringProjectsInArea, connection);
            /*
             DataAdapter and DataSet objects
            DataSet - in memory representation of data
            - it can contain multiple DataTable objects(columns and rows) and you can define relations
            - it's used by all DataProviders
            DataAdapter - contains a reference to a connection object;
            - open and closes automatically when reading/writing to db
            - contains commands for select, insert, delete, update
            - one DataAdapter defined for each table in DataSet; it does all the comm with the database
            */
            SqlDataAdapter daAreas = new SqlDataAdapter(selectAreas, connection);
            DataSet areasDataSet = new DataSet();
            //populate areasDataSet with data from areas table
            daAreas.Fill(areasDataSet, "areas");
            foreach(DataRow row in areasDataSet.Tables["areas"].Rows)
            {
                Console.WriteLine("{0}, {1}, {2}, {3}", row[0], row[1], row[2], row[3]);
            }   
        }
    }
}
