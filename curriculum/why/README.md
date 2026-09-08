# Answering «Навіщо мені це вчити?»

The most common question a 12-year-old asks, and the one the standard answers
fail hardest at. «Розвиває мислення», «знадобиться в житті» and «так треба» all
mean *I do not have a real answer*, and he can hear that.

One file per subject holds the honest answer for each topic. The tutor reads
the file for today's topic before the lesson, and answers from it when asked.

| File | Subject | State |
|---|---|---|
| `algebra.md` | Алгебра | Worked example — topics need checking against the textbook |
| `physics.md` | Фізика | To write |
| `chemistry.md` | Хімія | To write |
| `english.md` | Англійська | To write |

## The rules

1. Three sentences, maximum. Concrete.
2. Banned: «розвиває мислення», «знадобиться в житті», «буде на іспиті» as the
   *first* answer.
3. Answer in this order of preference:

   | Order | Kind of answer | Example |
   |---|---|---|
   | 1 | What breaks without it | «Без відсотків тебе обдурять на знижці, і ти не помітиш» |
   | 2 | Where it works in the thing he said he wants to do | Only when the link is real — check `state/aspirations.md` |
   | 3 | What it unlocks next | «Без цього не візьмеш квадратні рівняння, а вони скрізь» |
   | 4 | The plain truth | «Прямого застосування мало. Це в програмі, і це передумова для наступної теми» |

4. **Never invent an application.** Some school topics genuinely have weak
   direct use, and dressing one up gets detected — after which every honest
   answer is suspect too. Answer 4 costs nothing and buys credibility for the
   topics where answer 1 is strong.
5. Never give the same wording twice for the same topic. He notices, and a
   memorised line reads as a script rather than a reason.
6. Log the question in `why_asked`. A topic he asks about repeatedly is a
   motivation problem, not a curiosity one.

## Why this is worth a file rather than improvisation

A model asked «навіщо?» mid-lesson will produce something plausible every time,
including for topics where the honest answer is number 4. Writing the answers
down in advance is what keeps rule 4 enforceable — and it lets the parent
disagree with an answer before the student hears it.

## Table format

| Column | Contents |
|---|---|
| Тема | Topic name as it appears in the textbook |
| Навіщо | The answer, in Ukrainian, as the student would hear it |
| Тип | `ламається` / `робота` / `відкриває` / `програма` — which rule it uses |

A subject whose table is mostly `програма` is a subject to re-examine. Either
the answers have not been thought about hard enough, or the topic order in that
course really is disconnected from anything, which is worth knowing.
