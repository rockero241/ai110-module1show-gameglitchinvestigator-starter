# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looks decent based on the front end, but once you start the game you realize that it has some issues on the back end

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  I noticed that it often gave the wrong hints, saying to go higher when the number was lower and vice versa.
  
  There's also negative scores which makes it extremely difficult to catch up when the right answers aren't guessed from the start. I'm not sure if that's an issue, or by design.

  Lastly, the new game controls are broken. You can try starting a new game and it updates the secret number, but nothing happens afterwards and you're unable to play another game after the first.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I was close on my original evaluations of the issues but Claude helped me find more issues and helped me understand them, such as there being an issue with the "new game" button based on the state.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Not a sepecific suggestion, but the AI wanted to take over from the begining and change everything in the file. So I had to ask it to slow down and analyze more, then let me tell it exactly what to change and change that and only that.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
By running the game again and manually testing the things that were broken

- Describe at least one test you ran (manual or using pytest)  
Testing the new game button after guessing the secret correctly

  and what it showed you about your code.
That it ran once I updated the issue with the state like Claude said

- Did AI help you design or understand any tests? How?
Yeah, it helped me validate my original assumption that the hints where flipped
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Due to a type conversion bug that would sometimes change the secret number to a string

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Imagine playing a game where every time you make a move the whole board resets and redraws itself. That's streamlit reruns, where the entire script runs from scratch whenever you type of click something. Session state is like having a notebook that remembers your game progress between the resets, so you don't lose everything on each rerun.

- What change did you make that finally gave the game a stable secret number?
Removed the condition that was converting the secret number to a string on even numbered attempts, which was causing inconsistent comparisons in the guess checking logic. It should always be an int.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I enojoyed using AI to understand the codebase before I did anything else or asked it to change anything

  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I like using AI to understand not to delegate my thinking. And it can be a great tool for getting up to speed, understanding a codebase or realizing why something works the way it does.

- What is one thing you would do differently next time you work with AI on a coding task?
I would tell the AI from the begining to always give reasoning and wait for me to ask it to change things before it tries going and changning my files

- In one or two sentences, describe how this project changed the way you think about AI generated code.
It showed me that AI can be very helpful for understanding existing codebases and refractoring, but it's very important to know what you're doing. Otherwise you can end up with AI modifying most of the files, which would make it very diffult to go back and trace bugs. I plan to keep learning how to use it effectively and responsibly.