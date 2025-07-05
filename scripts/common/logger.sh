#!/usr/bin/env bash
# logger.sh - 统一日志输出库
# 用于提供统一的日志输出格式，支持颜色、图标和时间戳

# 检测是否在终端环境或是否设置了NO_COLOR环境变量
if [[ -t 1 ]] && [[ -z "${NO_COLOR:-}" ]] && [[ -z "${CI:-}" ]]; then
  # 颜色定义
  COLOR_RESET="\033[0m"
  COLOR_RED="\033[0;31m"
  COLOR_GREEN="\033[0;32m"
  COLOR_YELLOW="\033[0;33m"
  COLOR_BLUE="\033[0;34m"
  COLOR_PURPLE="\033[0;35m"
  COLOR_CYAN="\033[0;36m"
  COLOR_GRAY="\033[0;37m"
  COLOR_BOLD="\033[1m"
else
  # 如果不在终端环境或设置了NO_COLOR，则不使用颜色
  COLOR_RESET=""
  COLOR_RED=""
  COLOR_GREEN=""
  COLOR_YELLOW=""
  COLOR_BLUE=""
  COLOR_PURPLE=""
  COLOR_CYAN=""
  COLOR_GRAY=""
  COLOR_BOLD=""
fi

# 获取当前时间戳
get_timestamp() {
  date "+%H:%M:%S"
}

# 信息日志 - 蓝色
log_info() {
  echo -e "${COLOR_BLUE}[$(get_timestamp)] ℹ INFO:${COLOR_RESET} $*"
}

# 成功日志 - 绿色
log_success() {
  echo -e "${COLOR_GREEN}[$(get_timestamp)] ✅ SUCCESS:${COLOR_RESET} $*"
}

# 警告日志 - 黄色
log_warn() {
  echo -e "${COLOR_YELLOW}[$(get_timestamp)] ⚠️ WARNING:${COLOR_RESET} $*"
}

# 错误日志 - 红色
log_error() {
  echo -e "${COLOR_RED}[$(get_timestamp)] ❌ ERROR:${COLOR_RESET} $*" >&2
}

# 调试日志 - 灰色，仅在DEBUG=1时显示
log_debug() {
  if [[ "${DEBUG:-0}" == "1" ]]; then
    echo -e "${COLOR_GRAY}[$(get_timestamp)] 🔍 DEBUG:${COLOR_RESET} $*"
  fi
}

# 重要信息 - 紫色
log_important() {
  echo -e "${COLOR_PURPLE}[$(get_timestamp)] 📌 IMPORTANT:${COLOR_RESET} $*"
}

# 分隔线
log_divider() {
  local width=${1:-50}
  printf "%${width}s\n" | tr " " "-"
}

# 标题 - 加粗
log_title() {
  echo -e "\n${COLOR_BOLD}[$(get_timestamp)] 📋 $*${COLOR_RESET}"
  log_divider
} 