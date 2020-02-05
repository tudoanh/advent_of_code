defmodule Day1 do
  defp fuel(mass), do: Float.floor(mass / 3, 0) - 2

  def part1() do
    File.read!("input.txt")
    |> String.trim()
    |> String.split()
    |> Enum.map(&String.to_integer/1)
    |> Enum.map(&fuel/1)
    |> Enum.sum()
    |> IO.puts()
  end

  def total(mass) when mass <= 0, do: 0
  def total(mass) when mass > 0, do: fuel(mass) + total(fuel(mass))

  def part2() do
    File.read!("input.txt")
    |> String.trim()
    |> String.split()
    |> Enum.map(&String.to_integer/1)
    |> Enum.map(&total/1)
    |> Enum.sum()
    |> IO.puts()
  end
end

Day1.part1()
Day1.part2()
