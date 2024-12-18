import { promises as fs } from "fs";

function isReportSafe(report) {
  let safe = true;

  for (let i = 0; i < report.length; i++) {
    const sign = Math.sign(report[1] - report[0]);

    if (i + 1 < report.length) {
      const diff = report[i + 1] - report[i];

      if (
        Math.abs(diff) > 3 ||
        sign !== Math.sign(report[i + 1] - report[i]) ||
        diff === 0
      ) {
        safe = false;
        break;
      }
    }
  }

  return safe;
}

async function main() {
  const input = await fs.readFile("input.txt", "utf8");
  const inputToArray = input
    .split("\n")
    .filter((val) => val)
    .map((val) =>
      val
        .trim()
        .split(" ")
        .map((num) => parseInt(num))
    );

  let safeReports = 0;

  inputToArray.forEach((row) => {
    for (let i = 0; i < row.length; i++) {
      const report = row.slice(0);
      report.splice(i, 1);

      if (isReportSafe(report)) {
        safeReports += 1;
        break;
      }
    }
  });

  console.log(safeReports);
}

main();
