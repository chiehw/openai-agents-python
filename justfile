# Justfile for OpenAI Agents Python项目
# 使用方法:
# - `just agent` - 运行默认agent (filesystem_example)
# - `just agent path/to/agent.py` - 运行指定agent
# - `just agent path/to/agent.py --arg1 --arg2` - 带参数运行agent

# 默认运行 filesystem_example
agent DEFAULT="examples/mcp/filesystem_example/main.py":
    @chmod +x scripts/run_agent.sh
    @scripts/run_agent.sh {{DEFAULT}}

# 列出所有可用的examples
list-examples:
    @find examples -name "main.py" | sort 