using System;
using System.Collections.Generic;
using NUnit.Framework;

namespace GiesProgrammingExercise
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("To run more tests, use the command \"dotnet test\".");
            
            var list = new List<string>();
            string[] testOne = {"4", "6", "10", "", "0", "5"};
            PrintCases(testOne, list, 25);

            string[] testTwo = {"", "4", "", ""};
            PrintCases(testTwo, list, 4);

            string[] testThree = {"", ""};
            PrintCases(testThree, list, 0);
        }

        public static void PrintCases(string[] test, List<string> list, int expected)
        {
            list.Clear();
            list.AddRange(test);
            Console.WriteLine("test string values: [\"{0}\"]", string.Join("\", \"", test));
            Console.WriteLine("actual: {0}", TotalStringValues(list));
            Console.WriteLine("expected: {0}\n", expected);
        }

        public static int TotalStringValues(IEnumerable<string> list)
        {
            int sum = 0;
            foreach (string str in list)
            {
                if (String.Equals(str, ""))
                {
                    continue;
                }
                else
                {
                    int addend = 0;
                    Int32.TryParse(str, out addend);
                    sum += addend;
                }
            }
            return sum;
        }
    }

    [TestFixture]
    class ProgramTests
    {
        [TestCase(0, new string[] {""}, TestName="empty_string")]
        [TestCase(0, new string[] {"0"}, TestName="zero_string")]
        [TestCase(0, new string[] {"d34s"}, TestName="invalid_string_letters")]
        [TestCase(0, new string[] {"23.1"}, TestName="invalid_string_decimal")]
        [TestCase(-30000, new string[] {"-30000"}, TestName="negative_string")]
        [TestCase(405930, new string[] {"405930"}, TestName="positive_string")]
        [TestCase(25, new string[] {"4", "6", "10", "", "0", "5"}, TestName="positive_and_empty")]
        [TestCase(4, new string[] {"", "4", "", ""}, TestName="multiple_empty_strings")]
        [TestCase(4, new string[] {"132", "-128"}, TestName="positive_and_negative")]
        [TestCase(132, new string[] {"130", "2", "pea"}, TestName="positive_and_invalid_letters")]
        [TestCase(132, new string[] {"130", "2", "0.33"}, TestName="positive_and_invalid_decimal")]
        [TestCase(-94, new string[] {"-94", ""}, TestName="negative_and_empty")]
        [TestCase(-94, new string[] {"-94", "doop"}, TestName="negative_and_invalid_letters")]
        [TestCase(-94, new string[] {"-94", "94.8"}, TestName="negative_and_invalid_decimal")]
        [TestCase(0, new string[] {"p90x", ""}, TestName="invalid_letters_and_empty")]
        [TestCase(0, new string[] {"kdkdkd", "35.0"}, TestName="invalid_letters_and_invalid_decimal")]
        [TestCase(0, new string[] {"34.5", ""}, TestName="invalid_decimals_and_empty")]
        [TestCase(-1, new string[] {"4", "-5", ""}, TestName="positive_and_negative_and_empty")]
        [TestCase(-112, new string[] {"500", "-612", "3pol"}, TestName="positive_and_negative_and_invalid_letters")]
        [TestCase(-112, new string[] {"500", "-612", "3.44"}, TestName="positive_and_negative_and_invalid_decimal")]
        [TestCase(500, new string[] {"500", "3pol"}, TestName="positive_and_empty_and_invalid_letters")]
        [TestCase(35, new string[] {"039", "-4", "", "0", "23s", "45.5", "!!!!"}, TestName="everything")]
        [TestCase(0, new string[] {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "<", "\\"}, TestName="special_characters")]

        public void TotalStringValuesTest(int solution, string[] list)
        {
            Console.WriteLine(list);
            var result = Program.TotalStringValues(new List<string>(list));
            Assert.AreEqual(solution, result);
        }
    }
}