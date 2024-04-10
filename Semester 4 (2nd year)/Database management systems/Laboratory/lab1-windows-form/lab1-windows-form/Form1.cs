using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data;
using System.Data.SqlClient;
using System.Configuration;


namespace lab1_windows_form
{
    public partial class Form1 : Form
    {
        SqlConnection myConnection;
        SqlDataAdapter daParent;
        SqlDataAdapter daChild;
        DataSet myDataSet;
        BindingSource bsParent;
        BindingSource bsChild;

        SqlCommandBuilder myCommandBuilder;

        //string parentTable = ConfigurationSettings.AppSettings[parentTable];
        String parentTable;
        String childTable;
        String foreignKey;

        String queryParent;
        String queryChild; 

        public Form1()
        {
            InitializeComponent();
            FillData();
        }

        void FillData()
        {
            parentTable = ConfigurationManager.AppSettings["parentTable"];
            childTable = ConfigurationManager.AppSettings["childTable"];
            foreignKey = ConfigurationManager.AppSettings["foreignKey"];

            queryParent = $"SELECT * FROM {parentTable}";
            queryChild = $"SELECT * FROM {childTable}";


            //SQLConnection
            myConnection =
                new SqlConnection(getConnectionString());

            //SqlDataAdapter (for parent table and child table), DataSet
            daParent = new SqlDataAdapter(queryParent, myConnection);
            daChild = new SqlDataAdapter(queryChild, myConnection);
            myDataSet = new DataSet();
            daParent.Fill(myDataSet, parentTable);
            daChild.Fill(myDataSet, childTable);

            //fill in insert, update, delete commands
            myCommandBuilder = new SqlCommandBuilder(daChild);

            //DataRelation (parent-child rel) added to the DataSet
            DataRelation drAreasDLCs = new DataRelation("tableRelation",
                               myDataSet.Tables[parentTable].Columns[foreignKey],
                                              myDataSet.Tables[childTable].Columns[foreignKey]);
            myDataSet.Relations.Add(drAreasDLCs);

            //Method 1:
            // fill data into the DataGridView using 
            // the properties DataSource, DataMember
            this.GridGames.DataSource = myDataSet.Tables[parentTable];
            this.GridDLCs.DataSource = this.GridGames.DataSource;
            this.GridDLCs.DataMember = "tableRelation";
            // so from what I understand, it gets the data from the Games table
            // and then it gets the data from the DLCs table that is related to the Games table

            //Method 2:
            //fill data into the DataGridView using method2: using DataBinding
            /* bsParent = new BindingSource();
             bsParent.DataSource = myDataSet.Tables["Games"];
             bsChild = new BindingSource(bsParent, "GamesDLCs");

             this.GridGames.DataSource = bsParent;
             this.GridDLCs.DataSource = bsChild;*/

            /*
             * insert, update, delete commands: via SqlDataAdapter properties
             * or with SqlCommandBuilder --> easier
             * SqlCommandBuilder has limitations: works for a simple select stmt on a single table
             * it won't work for joining 2/more tables or procedures
             */

            myCommandBuilder.GetUpdateCommand();
        }

        string getConnectionString()
        {
            return "Data Source=GT-Lenovo\\SQLEXPRESS;" +
                "Initial Catalog=Steam;" +
                "Integrated Security=True;";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            try { 
                daChild.Update(myDataSet, childTable);
            }
            catch (Exception vsIsShit)
            {
                MessageBox.Show("The database update did not work \n" + vsIsShit.Message, "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Made the button connect and fill the data
            /* 
            myConnection = new SqlConnection(getConnectionString());
            myDataSet = new DataSet();
            daParent = new SqlDataAdapter(queryParent, myConnection);
            daChild = new SqlDataAdapter(queryChild, myConnection);
            daParent.Fill(myDataSet, "Games");
            daChild.Fill(myDataSet, "DLCs");

            //DataRelation (parent-child rel) added to the DataSet
            DataRelation drGamesDLCs = new DataRelation("tableRelation",
                               myDataSet.Tables["Games"].Columns["game_id"],
                                              myDataSet.Tables["DLCs"].Columns["game_id"]);
            myDataSet.Relations.Add(drGamesDLCs);

            bsParent = new BindingSource();
            bsChild = new BindingSource();

            bsParent.DataSource = myDataSet;
            bsParent.DataMember = "Games";

            bsChild.DataSource = bsParent;
            bsChild.DataMember = "DLCs";

            this.GridGames.DataSource = bsParent;
            this.GridDLCs.DataSource = bsChild;*/
        }

        private void GridProjects_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
