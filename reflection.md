# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
---
I entered the program with a well thought our strategy of implementing binary search as my technique to reach the target number the fastest. However, there were several glitches. First, the program would always respond to my guess with "guess higher" instead of "guess lower" when my guess was too high. In addition, The range was the same for each difficulty, and the range should have been different for "easy", "medium", and "hard" logically in a game like this. Furthermore, the guess attempts for the "easy" and "normal" diffulties were swapped where "normal" had eight guesses while "easy" had only six guesses.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
---
I utilized Copilot on this project and did not require the help of ChatGPT, Gemini, or other generative agents for assistance. I first asked Copilot to refactor each of the four functions from app.py to logic_utils.py and the agent gave an updated file design for logic_utils.py that I was satisifed with, and therefore, used. Copilot's suggest was correct here and the response worked accurately within the scope of the project. I verified by cross checking my old logic_utils.py file's empty function headers with the new ones and ensuring that the four functions were the same as the original in app.py when they were refactored into the new file. Later, I asked Copilot to fix the high/low issue and giving it context of both files. Copilot suggested that I modify a large piece of my app.py file but when I copy and pasted the response, my code broke. Copilot wanted to update how the program behaved with the user's guess alone rather and focused seemingly only on app.py even though it should have referenced the four function (parameters, specifically)Copilot's suggest was extremely misleading.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
---
I decided whether a bug was really fix by going through both app.py and logic_utils.py (mostly app.py fully) and running the game after every fix to ensure that the bug I was focusing on was dealt with. I ran the function tests to make sure the functions were running correctly, and I determined what the functions did by looking at their results and their parameters. Yes, Copilot helped me design the test for test_check_guess when I gave it the context as suggested in the assignment.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
---
I learned that Streamlight is a tool that can be used to develop and run projects such as this game. I learned that state is an attribue of Streamlit. When the program is runed with Streamlit, the attribute state essentially incorporates the current run or "state's" values inside it and then this variable can be used to house all other variables that are important for the game in one user run as the program used it.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  ---
I want to continue leveraging live AI agents to optimize and generate impactful program compliments for future program enhancement and success.
- What is one thing you would do differently next time you work with AI on a coding task?
---
The nex time I work with AI on a coding task, I will first complete the coding task myself and then if I need help, I will resort to the AI agent instead of depending on the AI agent first and/or entirely.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
---
Because of this project, I now view AI generated code as modifications or enhancements to human developed code rather than simply having AI write code for humans. I find it imperative for humans to use their own "human-centric" ideas to generate publicly impacting code and then refining it using AI instead of letting AI take the lead on the programming itself.
