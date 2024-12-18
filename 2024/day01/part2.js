import { promises as fs } from "fs";

function occInArr(arr, check) {
  let occurances = 0;

  arr.forEach((num) => num === check && occurances++);

  return occurances;
}

async function main() {
  const input = await fs.readFile("input.txt", "utf8");
  const inputToArray = input.split("\n").filter((val) => val);

  const lists = [[], []];

  inputToArray.forEach((row) => {
    const numbers = row.split("\r")[0].split("   ");
    lists[0].push(numbers[0]);
    lists[1].push(numbers[1]);
  });

  let total = 0;

  lists[0].forEach((num) => {
    total += num * occInArr(lists[1], num);
  });

  console.log(total);
}

main();
