import { promises as fs } from "fs";

async function main() {
  const input = await fs.readFile("sample-input.txt", "utf8");

  const matches = [...input.matchAll(/mul\([0-9,]{0,10}\)/gi)].map((x) =>
    x[0]
      .split("mul(")[1]
      .split(")")[0]
      .split(",")
      .map((x) => parseInt(x))
  );

  const multiply = matches.map((x) => x[0] * x[1]).filter(Boolean);

  const sum = multiply.reduce((acc, cur) => acc + cur, 0);

  console.log(sum);
}

main();
