using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static void Main(string[] args)
    {
        ToggleFeatures toggelFeatures = new ToggleFeatures();

        // Add features with their respective functions and with a status that we choose
        toggelFeatures.AddFeature("FEATURE1", Tests.Feature1, true);
        toggelFeatures.AddFeature("FEATURE2", Tests.Feature2, false);
        toggelFeatures.AddFeature("FEATURE3", Tests.Feature3, true);

        // Execute feature functions based on feature state
        toggelFeatures.ExecuteFeatureFunction("FEATURE1");
        toggelFeatures.ExecuteFeatureFunction("FEATURE2"); // Should display a message that it's not enabled
        toggelFeatures.ExecuteFeatureFunction("FEATURE3");

        // Toggle Feature2 and execute its function again
        toggelFeatures.ToggleFeature("FEATURE2");
        toggelFeatures.ExecuteFeatureFunction("FEATURE2"); // Changed, so now it executes

        // Toggle Feature1 and try executing its function again
        toggelFeatures.ToggleFeature("FEATURE1");
        toggelFeatures.ExecuteFeatureFunction("FEATURE1"); // Should display a message that it's not enabled
    }
}