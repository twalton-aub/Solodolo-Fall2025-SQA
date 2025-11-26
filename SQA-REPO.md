# Activities (excluding general setup):
## Fuzzing Integration (fuzz.py):
Created a fuzz.py script that automatically fuzzes five Python functions throughout the project.

Used randomized input generation and simple mutations based on techniques learned in class/workshop.

Ensured that the script saves crash information into the output folder/txt (only in the envronment it is executed in | only in Github Actions by instructions).

Verified that fuzz.py runs automatically through GitHub Actions on every push/change.

Verfied that crashes did happen (seen in details of workflow runs in Github Actions).

## Forensic Logging Integration (FAME_ML's main.py):
Added forensic-style logging statements to five Python functions in main.py in the FAME_ML folder.

About 10 loggings were stated throughout the file pertaining to the order and contents of the functions.

Logging was kept simple and readable to avoid noise.

## Continuous Integration (Github Actions):
Added a workflow file under .github/workflows/fuzz.yml in the root.

On every commit or pull request:

  Python is set up

  Dependencies are installed

  fuzz.py is executed

  Output is logged in the workflow

# Lessons Learned:
Throughout this project, the biggest lesson came from dealing with problems caused by inconsistent/poor file and folder naming within the imported MLForensics project. What initially seemed like a simple setup became unexpectedly difficult because several files used non-standard naming styles and mismatched directory paths that did not align with how Python expects modules to be structured. Then unnecessary empty folder holding the main folder made the work progression on this even more annoying in the fuzz steps and navigation. These small inconsistencies caused import failures, prevented the fuzz.py script from running correctly, and repeatedly broke the GitHub Actions workflow. The continuous integration pipeline ended up being the most valuable tool in diagnosing these issues: every time the workflow failed, it pointed directly to missing-modules/errors, incorrect paths, or poorly-named/unfound files. This forced a deeper understanding of how Python resolves imports, why naming conventions matter, and how CI exposes issues that do not appear locally. By carefully correcting file names, adding needed files, adjusting imports, and making the structure consistent (with what was worked on). The project eventually ran smoothly and finished accordingly by the standards of the understanding of the instructions. This experience emphasized that clean file/folder organization is not just style; it directly affects tooling, automation, and maintainability. It also showed that CI, fuzzing, and logging works together: CI revealed structural problems, fuzzing revealed potential runtime issues, and that logging can help explain unexpected behavior. Overall, the project demonstrated how essential consistency, automation, and incremental debugging are when integrating multiple SQA activities into a real codebase.
