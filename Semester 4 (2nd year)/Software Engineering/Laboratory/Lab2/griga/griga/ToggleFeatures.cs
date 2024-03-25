//featuretoggleclass
using System;
using System.Collections.Generic;
//Action is a delegate type that can refference methods

/*
 * ToggleFeatures{
    featureActions - dict, stores feature name and it's action
    featureStates - dict, store feature name and it's state ( flase - not active, true - active )
}
 */
public class ToggleFeatures
{
    private Dictionary<string, Action<object[]>> featureActions;
    private Dictionary<string, bool> featureStates;

    public ToggleFeatures()
    {
        featureActions = new Dictionary<string, Action<object[]>>();  
        featureStates = new Dictionary<string, bool>(); 
    }
    /*
     * AddFeature
     fuction to add a feature, has 3 parameters: string name of feature, Action name of function and a bool value
    */

    public void AddFeature(string featureName, Action<object[]> featureAction, bool featureState) 
    {
        if (!featureActions.ContainsKey(featureName)) 
        {
            featureActions.Add(featureName, featureAction);
            featureStates.Add(featureName, featureState);  
        }
        else
        {
            featureActions[featureName] = featureAction;
            featureStates[featureName] = featureState; 
        }
    }
    /*
     ExecuteFeatureFunction
    function to execute features that are enabled, has as a parameter the name of the feature as string
    */

    public void ExecuteFeatureFunction(string featureName, params object[] parameters)
    {
        if (featureActions.ContainsKey(featureName) && featureStates[featureName])
        {
            featureActions[featureName](parameters); 
        }
        else
        {
            Tests.FeatureDisabledText(parameters); 
        }
    }
    /*
     * ToggleFeature
     * function to change the state of a feature, has as a parameter the name of the feature as string
     */

    public void ToggleFeature(string featureName) 
    {
        if (featureStates.ContainsKey(featureName)) 
        {
            featureStates[featureName] = !featureStates[featureName];
        }
    }
}