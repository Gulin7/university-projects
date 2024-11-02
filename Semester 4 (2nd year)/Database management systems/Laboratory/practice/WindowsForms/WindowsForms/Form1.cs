using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsForms
{
    public partial class Form1 : Form
    {
        SqlConnection conn;
        SqlDataAdapter daMembers;
        SqlDataAdapter daTasks;
        DataSet dataSet;
        BindingSource bsMembers;
        BindingSource bsTasks;

        SqlCommandBuilder commandBuilder;

        string queryMembers;
        string queryTasks;
        public Form1()
        {
            InitializeComponent();
            FillData();
        }

        void FillData()
        {
            conn = new SqlConnection(getConnectionString());
            
            queryMembers = "SELECT * FROM Brokerage";
            queryTasks = "SELECT * FROM Clients";

            daMembers = new SqlDataAdapter(queryMembers, conn);
            daTasks = new SqlDataAdapter(queryTasks, conn);
            dataSet = new DataSet();
            daMembers.Fill(dataSet, "Brokerage");
            daTasks.Fill(dataSet, "Clients");

            commandBuilder = new SqlCommandBuilder(daMembers);
            commandBuilder = new SqlCommandBuilder(daTasks);

            dataSet.Relations.Add("BrokerClient", dataSet.Tables["Brokerage"].Columns["brokerId"], 
                                                 dataSet.Tables["Clients"].Columns["brokerId"]); 

            //METOD 1: fill data into DataGridViews using the properties DataSource and DataMember  
            this.dgvMembers.DataSource = dataSet.Tables["Brokerage"];
            this.dgvTasks.DataSource = this.dgvMembers.DataSource;
            this.dgvTasks.DataMember = "BrokerClient";
            
            commandBuilder.GetUpdateCommand();
        }

        private string getConnectionString()
        {
            return "Data Source=GT-LENOVO\\SQLEXPRESS;" +
                "Initial Catalog=PracticalExam;" 
                    + "Integrated Security=True;";
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                daMembers.Update(dataSet, "Brokerage");
                daTasks.Update(dataSet, "Clients");
            }
            catch (Exception ex)
            {
                MessageBox.Show("An error occurred while updating the database: " + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
