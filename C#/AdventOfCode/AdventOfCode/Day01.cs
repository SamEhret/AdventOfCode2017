using System;

namespace day01project
{
    public class Day01
    {
        public void Run()
        {
            string input = System.IO.File.ReadAllText("day01input.txt");

            Part1(input);
            Part2(input);
        }

        private void Part1(string input)
        {
            int sum = 0;
            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] == input[(i + 1) % input.Length])
                {
                    sum += Int32.Parse(input[i].ToString());
                }
            }
            Console.WriteLine("Part 1 Answer: " + sum);
        }

        private void Part2(string input)
        {
            int sum = 0;
            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] == input[(i + (input.Length / 2)) % input.Length])
                {
                    sum += Int32.Parse(input[i].ToString());
                }
            }
            Console.WriteLine("Part 2 Answer: " + sum);
        }
    }
}