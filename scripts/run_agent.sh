#!/usr/bin/env bash

# 导入通用日志库
. "$(dirname "$BASH_SOURCE")/common/logger.sh"

# 确保脚本出错时立即退出
set -e

# 获取脚本所在目录的绝对路径
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

# TODO: 校验 uv 是否安装
# if ! command -v uv &> /dev/null; then
#     log_error "检测到 uv 未安装，请先执行 'pip install uv' 或其他安装方式"
#     exit 1
# fi

# 解析第一个参数为agent路径，如果没有提供则使用默认路径
AGENT_PATH="${1:-examples/mcp/filesystem_example/main.py}"

# 如果路径不是绝对路径，则相对于项目根目录解析
if [[ ! "$AGENT_PATH" = /* ]]; then
    AGENT_PATH="$PROJECT_ROOT/$AGENT_PATH"
fi

log_info "正在启动 Agent: $AGENT_PATH"

# 使用uv运行Python脚本，并传递除第一个参数外的所有参数
log_info "执行 uv run ..."
cd "$PROJECT_ROOT" && uv run python "$AGENT_PATH" "${@:2}" 
log_success "Agent 运行结束" 