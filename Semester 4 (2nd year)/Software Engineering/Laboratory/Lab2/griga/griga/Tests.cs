﻿//testfunctions
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Tests //calss for our feature function that we will run tests on
{
    public static void Feature1(params object[] parameters) //function that displays a message
    {
        Console.WriteLine("Feature 1 is enabled and executed.");
    }

    public static void Feature2(params object[] parameters)//function that displays a message
    {
        Console.WriteLine("Feature 2 is enabled and executed.");
    }

    public static void Feature3(params object[] parameters)//function that displays a message
    {
        Console.WriteLine("Feature 3 is enabled and executed.\n");
    }

    public static void FeatureDisabledText(params object[] parameters)//function that displays a message for the case of not enabled or not existent
    {
        Console.WriteLine("This feature is not enabled so it doesn't work");
    }

    public static void FeatureWriteText(params object[] parameters)
    {
        string text = "";
        for (int i = 0; i < parameters.Length; i++)
        {
            text += (string)parameters[i];
        }   
        Console.WriteLine(text);
    }
}