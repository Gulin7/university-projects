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


namespace lab1_windows_form
{
    public partial class Form1 : Form
    {
        SqlConnection myConnection;
        SqlDataAdapter daGames;
        SqlDataAdapter daDLCs;
        DataSet myDataSet;
        BindingSource bsGames;
        BindingSource bsDLCs;

        SqlCommandBuilder myCommandBuilder;

        string queryGames = "SELECT * FROM Games";
        string queryDLCs = "SELECT * FROM DLCs";

        public Form1()
        {
            InitializeComponent();
            FillData();
        }

        void FillData()
        {
            //SQLConnection
            myConnection =
                new SqlConnection(getConnectionString());

            //SqlDataAdapter (for parent table and child table), DataSet
            daGames = new SqlDataAdapter(queryGames, myConnection);
            daDLCs = new SqlDataAdapter(queryDLCs, myConnection);
            myDataSet = new DataSet();
            daGames.Fill(myDataSet, "Games");
            daDLCs.Fill(myDataSet, "DLCs");

            //fill in insert, update, delete commands
            myCommandBuilder = new SqlCommandBuilder(daDLCs);

            //DataRelation (parent-child rel) added to the DataSet
            DataRelation drAreasDLCs = new DataRelation("GamesDLCs",
                               myDataSet.Tables["Games"].Columns["game_id"],
                                              myDataSet.Tables["DLCs"].Columns["game_id"]);
            myDataSet.Relations.Add(drAreasDLCs);

            //Method 1:
            // fill data into the DataGridView using 
            // the properties DataSource, DataMember
            this.GridGames.DataSource = myDataSet.Tables["Games"];
            this.GridDLCs.DataSource = this.GridGames.DataSource;
            this.GridDLCs.DataMember = "GamesDLCs";
            // so from what I understand, it gets the data from the Games table
            // and then it gets the data from the DLCs table that is related to the Games table

            //Method 2:
            //fill data into the DataGridView using method2: using DataBinding
            /* bsGames = new BindingSource();
             bsGames.DataSource = myDataSet.Tables["Games"];
             bsDLCs = new BindingSource(bsGames, "GamesDLCs");

             this.GridGames.DataSource = bsGames;
             this.GridDLCs.DataSource = bsDLCs;*/

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
                daDLCs.Update(myDataSet, "DLCs");
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
            daGames = new SqlDataAdapter(queryGames, myConnection);
            daDLCs = new SqlDataAdapter(queryDLCs, myConnection);
            daGames.Fill(myDataSet, "Games");
            daDLCs.Fill(myDataSet, "DLCs");

            //DataRelation (parent-child rel) added to the DataSet
            DataRelation drGamesDLCs = new DataRelation("GamesDLCs",
                               myDataSet.Tables["Games"].Columns["game_id"],
                                              myDataSet.Tables["DLCs"].Columns["game_id"]);
            myDataSet.Relations.Add(drGamesDLCs);

            bsGames = new BindingSource();
            bsDLCs = new BindingSource();

            bsGames.DataSource = myDataSet;
            bsGames.DataMember = "Games";

            bsDLCs.DataSource = bsGames;
            bsDLCs.DataMember = "DLCs";

            this.GridGames.DataSource = bsGames;
            this.GridDLCs.DataSource = bsDLCs;*/
        }

        private void GridProjects_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
