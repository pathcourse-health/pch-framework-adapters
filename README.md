# PCH Framework Adapters

Six thin OpenAI-compatibility wrappers letting developers use PathCourse Health from the AI
agent frameworks they already use. Each subdirectory is its own publishable package.

The PCH gateway at `https://gateway.pathcoursehealth.com/v1` is fully OpenAI API-compatible.
Every adapter is a thin layer that points the framework's existing OpenAI integration at the
PCH gateway. A developer with 10,000 lines of LangChain code switches by changing one line.

## Packages

| Package | Ecosystem | Registry | Source |
|---|---|---|---|
| [`langchain-pathcourse`](https://pypi.org/project/langchain-pathcourse/) | LangChain (Python) | PyPI | [`langchain-pathcourse/`](./langchain-pathcourse) |
| [`@pathcourse/langchain`](https://www.npmjs.com/package/@pathcourse/langchain) | LangChain (JS) | npm | [`langchain-pathcourse-js/`](./langchain-pathcourse-js) |
| [`@pathcourse/ai`](https://www.npmjs.com/package/@pathcourse/ai) | Vercel AI SDK (Next.js) | npm | [`pathcourse-ai-sdk/`](./pathcourse-ai-sdk) |
| [`crewai-pathcourse`](https://pypi.org/project/crewai-pathcourse/) | CrewAI | PyPI | [`crewai-pathcourse/`](./crewai-pathcourse) |
| [`pydantic-ai-pathcourse`](https://pypi.org/project/pydantic-ai-pathcourse/) | Pydantic AI | PyPI | [`pydantic-ai-pathcourse/`](./pydantic-ai-pathcourse) |
| [`autogen-pathcourse`](https://pypi.org/project/autogen-pathcourse/) | AutoGen / AG2 | PyPI | [`autogen-pathcourse/`](./autogen-pathcourse) |

## Working examples

Step-by-step examples for every adapter live in the
[`pch-integration-examples`](https://github.com/pathcourse-health/pch-integration-examples)
repo under `frameworks/`. Start there if you're new to PCH.

## Publishing a new version

### Python (PyPI)

```bash
cd <package-dir>                      # langchain-pathcourse, crewai-pathcourse, etc.
python -m build
python -m twine check dist/*
python -m twine upload dist/*         # production PyPI (set TWINE_USERNAME=__token__, TWINE_PASSWORD=<token>)
```

### TypeScript (npm)

```bash
cd <package-dir>                      # langchain-pathcourse-js or pathcourse-ai-sdk
npm install
npm run build
npm publish --dry-run                 # inspect what will ship
npm publish --access public           # 2FA OTP prompt
```

## Verifying a new release

```bash
pip install <package-name>
python -c "from <module> import <Class>; print('OK')"

npm install <@scope/name>
node -e "const p = require('<@scope/name>'); console.log('OK')"
```

## Versioning

Each package version is independent. The PCH SDK at `pathcourse-sdk` / `@pathcourse/sdk` is
on a separate version track. Bump only the packages you actually changed.

## Repository layout

```
pch-framework-adapters/
├── README.md                       # this file
├── LICENSE
├── .gitignore
├── langchain-pathcourse/           # Python — extends ChatOpenAI
├── langchain-pathcourse-js/        # TypeScript — extends ChatOpenAI
├── pathcourse-ai-sdk/              # TypeScript — Vercel AI SDK provider
├── crewai-pathcourse/              # Python — wraps CrewAI's LLM
├── pydantic-ai-pathcourse/         # Python — wraps OpenAIModel
└── autogen-pathcourse/             # Python — config_list builder
```

## License

MIT — see [LICENSE](./LICENSE).
