import { promises as fs } from "fs";

async function main() {
  const input = await fs.readFile("input.txt", "utf8");
  // const inputToArray = input.split("\n").filter((val) => val).map((val) => val.split("\r")[0]);
}

main();
