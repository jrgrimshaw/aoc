import { promises as fs } from "fs";

async function main() {
  const input = await fs.readFile("input.txt", "utf8");
  const inputToArray = input
    .split("\n")
    .filter((val) => val)
    .map((val) =>
      val
        .split("\r")[0]
        .split(" ")
        .map((num) => parseInt(num))
    );

  const safeReports = inputToArray.filter((report, i) => {
    let safe = true,
      increasing = false,
      decreasing = false;

    for (let i = 0; i < report.length; i++) {
      if (i + 1 < report.length) {
        const diff = report[i + 1] - report[i];

        if (
          Math.abs(diff) > 3 ||
          (increasing && diff < 0) ||
          (decreasing && diff > 1) ||
          diff === 0
        ) {
          safe = false;
          break;
        }

        if (diff > 0) increasing = true;
        else decreasing = true;
      }
    }

    return safe;
  });

  console.log(safeReports.length);
}

main();
