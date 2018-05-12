using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.IO;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Text.RegularExpressions;

namespace day04project
{
    public static class Day04
    {
        public static void Run()
        {
            var line = "";
            var input = new List<string>();
            var file = new StreamReader(@"day04input.txt");
            while((line = file.ReadLine()) != null)  
            {  
                input.Add(line);
            }

            Part01(input);
            Part02(input);
        }

        private static void Part01(IEnumerable<string> input)
        {
            var validCount = 0;
            var checkList = new List<string>();
            
            foreach (var line in input)
            {
                var tempLine = line.Split(null);
                checkList.Clear();
                
                foreach (var item in tempLine)
                {
                    if (!checkList.Contains(item))
                    {
                        checkList.Add(item);
                        if (tempLine.SequenceEqual(checkList))
                        {
                            validCount += 1;
                        }
                    }
                }
            }
            Console.WriteLine($"Part 1 Answer: {validCount}");
        }

        private static void Part02(IEnumerable<string> input)
        {
            var validCount = 0;
            var checkList = new List<string>();
            
            foreach (var line in input)
            {
                var tempLine = line.Split(null);
                checkList.Clear();
                
                foreach (var item in tempLine)
                {
                    var tempItem = new string (item.OrderBy(c => c).ToArray());

                    if (!checkList.Contains(tempItem))
                    {
                        checkList.Add(tempItem);
                        if (tempLine.Length == checkList.Count)
                        {
                            validCount += 1;
                        }
                    }
                }
            }
            Console.WriteLine($"Part 2 Answer: {validCount}");
        }
    }
}
