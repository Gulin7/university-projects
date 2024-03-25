using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static void Main(string[] args)
    {
        ToggleFeatures toggleFeatures = new ToggleFeatures();

        // Add features with their respective functions and with a status that we choose
        toggleFeatures.AddFeature("FEATURE1", Tests.Feature1, true);
        toggleFeatures.AddFeature("FEATURE2", Tests.Feature2, false);
        toggleFeatures.AddFeature("FEATURE3", Tests.Feature3, true);
        toggleFeatures.AddFeature("Feature Write Text", Tests.FeatureWriteText, true);

        object[] test = { "This is a test message\n" };

        // Execute feature functions based on feature state
        toggleFeatures.ExecuteFeatureFunction("FEATURE1");
        toggleFeatures.ExecuteFeatureFunction("FEATURE2"); // Should display a message that it's not enabled
        toggleFeatures.ExecuteFeatureFunction("FEATURE3");
        toggleFeatures.ExecuteFeatureFunction("Feature Write Text", test);

        // Toggle Feature2 and execute its function again
        toggleFeatures.ToggleFeature("FEATURE2");
        toggleFeatures.ExecuteFeatureFunction("FEATURE2"); // Changed, so now it executes

        // Toggle Feature1 and try executing its function again
        toggleFeatures.ToggleFeature("FEATURE1");
        toggleFeatures.ExecuteFeatureFunction("FEATURE1"); // Should display a message that it's not enabled

        Console.WriteLine("Trying to use feature write text after disabling it");
        toggleFeatures.ToggleFeature("Feature Write Text");
        toggleFeatures.ExecuteFeatureFunction("Feature Write Text", test); // Should display a message that it's not enabled
    }
}