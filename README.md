# FreeGPTAI

**FreeGPTAI** is a Python package that simplifies the process of generating text completions using OpenAI's GPT-3 model. With this package, you can easily interact with the GPT-3 API to create chatbot-like responses based on user prompts.

## Installation

You can install **FreeGPTAI** using `pip`:

```bash
pip install freegptai



## Quick Start

To get started with FreeGPTAI, follow these simple steps:

1. **Install the Package**:
   Install the FreeGPTAI package using `pip` as shown above.

2. **Create a Chatbot Instance and Generate Responses**:
   Now you can create a FreeGPTAI instance and generate responses based on prompts:

   ```python
   from freegptai import Completion

  async def main():
      completion = Completion()
      prompt = "Tell me a joke."
      generated_text = await completion.create(prompt)
      print(generated_text)
  
  if __name__ == "__main__":
      import asyncio
      asyncio.run(main())

3. **Explore Additional Configuration:**
   FreeGPTAI allows you to configure various parameters such as headers and URL. Check the documentation for details on advanced usage.


### Contributing
**We welcome contributions to FreeGPTAI! If you find a bug or have an enhancement in mind, please open an issue or submit a pull request on GitHub.**



**Enjoy building intelligent chatbots with FreeGPTAI!**

