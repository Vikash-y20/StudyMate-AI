# StudyMate AI Architecture

```text
Audio / PDF / Notes
        |
        v
Pre-processing / Speech-to-Text
        |
        v
Local AI Engine
(Summary / Q&A / Topics)
        |
        v
Notes / Questions / Flashcards
        |
        v
Student Dashboard
```

## Snapdragon implementation plan
1. Add a suitable Qualcomm AI Hub speech-to-text model.
2. Add a compact local language model for richer Q&A and summarization.
3. Optimize/compile supported models for the target Snapdragon platform.
4. Test on the actual HP Snapdragon PC.
5. Record measured latency, memory and responsiveness in the final submission.
