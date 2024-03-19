
internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Welcome to Temperature Converter!");

        ConvertTemperature();
    }

    static void ConvertTemperature()
    {
        int option;
        double temperature;

        while (true)
        {
            option = GetOption();
            temperature = GetTemperature();
            double result = 0;
            switch (option)
            {
                case 1:
                    result = CelsiusToFahrenheit(temperature);
                    Console.WriteLine("The temperature in Fahrenheit is: " + result);
                    break;
                case 2:
                    result = FahrenheitToCelsius(temperature);
                    Console.WriteLine("The temperature in Celsius is: " + result);
                    break;
                case 3:
                    result = CelsiusToKelvin(temperature);
                    Console.WriteLine("The temperature in Kelvin is: " + result);
                    break;
                case 4:
                    result = KelvinToCelsius(temperature);
                    Console.WriteLine("The temperature in Celsius is: " + result);
                    break;
                case 5:
                    result = FahrenheitToKelvin(temperature);
                    Console.WriteLine("The temperature in Kelvin is: " + result);
                    break;
                case 6:
                    result = KelvinToFahrenheit(temperature);
                    Console.WriteLine("The temperature in Fahrenheit is: " + result);
                    break;
                case 0:
                    Console.WriteLine("Goodbye!");
                    return;
                default:
                    Console.WriteLine("Invalid option!");
                    return;
            }

        }
    }
    static int GetOption()
    {
        int option;
        while (true)
        {
            try
            {
                Console.WriteLine("Enter an option: ");
                Console.WriteLine("1. Celsius to Fahrenheit");
                Console.WriteLine("2. Fahrenheit to Celsius");
                Console.WriteLine("3. Celsius to Kelvin");
                Console.WriteLine("4. Kelvin to Celsius");
                Console.WriteLine("5. Fahrenheit to Kelvin");
                Console.WriteLine("6. Kelvin to Fahrenheit");
                Console.WriteLine("0. Exit");

                Console.WriteLine("Enter an option: ");
                option = Convert.ToInt32(Console.ReadLine());
                break;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }

        }
        return option;
    }
    static double GetTemperature()
    {
        double temperature;
        while (true)
        {
            try
            {
                Console.WriteLine("Enter the temperature: ");
                temperature = Convert.ToDouble(Console.ReadLine());
                break;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
        return temperature;
    }
    // Conversion functions
    static double CelsiusToFahrenheit(double celsius)
    {
        return (celsius * 9 / 5) + 32;
    }

    static double FahrenheitToCelsius(double fahrenheit)
    {
        return (fahrenheit - 32) * 5 / 9;
    }

    static double CelsiusToKelvin(double celsius)
    {
        return celsius + 273.15;
    }

    static double KelvinToCelsius(double kelvin)
    {
        return kelvin - 273.15;
    }

    static double FahrenheitToKelvin(double fahrenheit)
    {
        return (fahrenheit + 459.67) * 5 / 9;
    }

    static double KelvinToFahrenheit(double kelvin)
    {
        return kelvin * 9 / 5 - 459.67;
    }
}