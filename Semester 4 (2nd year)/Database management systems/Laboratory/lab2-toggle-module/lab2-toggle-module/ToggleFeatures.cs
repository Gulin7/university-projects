//featuretoggleclass
using System;
using System.Collections.Generic;
//Action is a delegate type that can refference methods
public class ToggleFeatures
{
    private Dictionary<string, Action> featureActions;
    private Dictionary<string, bool> featureStates;

    public ToggleFeatures()
    {
        featureActions = new Dictionary<string, Action>();  //dictionary that assigns a func to a feature name, delegate is used to encapsulate a (void) method (assoc to each feat) as it doesnt return a val
        featureStates = new Dictionary<string, bool>(); //dictionary that assings the status of "disabled" or "enable" to a feature name
    }

    public void AddFeature(string featureName, Action featureAction, bool isEnabledOrNot) //fuction to add a feature, has 3 parameters: string name of feature, Action name of function and a bool value
    {
        if (!featureActions.ContainsKey(featureName)) //check if the feature is in our dictionary of functions
        {
            featureActions.Add(featureName, featureAction);
            featureStates.Add(featureName, isEnabledOrNot);  //if it doesn't we add it with the status of the bool value and function recieved as a parameter
        }
        else
        {
            featureActions[featureName] = featureAction;
            featureStates[featureName] = isEnabledOrNot; //if it already exists we update it with the funct parameters
        }
    }


    public void ExecuteFeatureFunction(string featureName)//function to execute features that are enabled, has as a parameter the name of the feature as string
    {
        if (featureActions.ContainsKey(featureName) && featureStates[featureName])
        {
            featureActions[featureName](); //run the function of the feature if it exists and it is enabled
        }
        else
        {
            FeatureTesterFunctions.FeatureDisabledText(); //call the FeatureDisabledText funciton that handles the case of a function being disabled or not existing 
        }
    }

    public void ToggleFeature(string featureName) //function to change the state of a feature, has as a parameter the name of the feature as string
    {
        if (featureStates.ContainsKey(featureName)) //see if the feature exists
        {
            featureStates[featureName] = !featureStates[featureName]; //if it does, toggle it to be dis to en or en to dis
        }
    }
}