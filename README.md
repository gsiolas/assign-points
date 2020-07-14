### If you used a form of type "quiz"

Edit line 11 of the script `assign-points.py` and specify the numbers of multiple-choice questions in `answers.json`. You can enter single numbers or ranges. Example: 

```python
rng = "12,27-69"
```

Edit lines 12-14 and assign points to all correct, wrong, and missing answers, so you don't have to do it manually for each question. Example:

```python
points_correct = 3
points_wrong = -1
points_missing = 0
```

#### First run

The first time you run

```bash
./assign-points.py answers.json
```

the script will create two files:

- `answers-wp.json`: a json file with points assigned to each question.
- `answers-corr.tsv`: this is a tab-separated values file. Format: question-number, question, correct-answer. After the first run, the 3rd field "correct-answer" will be empty. Edit the file, fill the correct answers in the 3rd field (without any quotes), and save `answers-corr.tsv`.

#### Second run

```bash
./assign-points.py answers.json
```

In the second run, the script will put the correct answers (strings) into `answers-wp.json`, based on  the edited `answers-corr.tsv`.

If you want to restart the procedure, delete the file `answers-corr.tsv`.

You can use any filename instead of "answer."