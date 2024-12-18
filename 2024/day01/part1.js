import { promises as fs } from "fs";

async function main() {
  const input = await fs.readFile("input.txt", "utf8");
  const inputToArray = input.split("\n").filter((val) => val);

  const lists = [[], []];
  let totalDistances = 0;

  inputToArray.forEach((row) => {
    const numbers = row.split("\r")[0].split("   ");
    lists[0].push(numbers[0]);
    lists[1].push(numbers[1]);
  });

  lists[0].sort();
  lists[1].sort();

  for (let i = 0; i < lists[0].length; i++) {
    totalDistances += Math.abs(lists[0][i] - lists[1][i]);
  }

  console.log(totalDistances);
}

main();
