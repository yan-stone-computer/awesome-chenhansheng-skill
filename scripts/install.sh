#!/usr/bin/env bash
# ============================================================
# awesome-chen-hansheng 一键安装脚本
# 支持: WorkBuddy / Claude Code / Cursor / OpenCode / Trae
# 用法:
#   bash scripts/install.sh --workbuddy
#   bash scripts/install.sh --claude-code
#   bash scripts/install.sh --cursor
#   bash scripts/install.sh --opencode
#   bash scripts/install.sh --trae
#   bash scripts/install.sh --all
# ============================================================

set -euo pipefail

# 颜色输出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

log()  { echo -e "${GREEN}[✓]${NC} $1"; }
warn() { echo -e "${YELLOW}[!]${NC} $1"; }
info() { echo -e "${CYAN}[>]${NC} $1"; }
fail() { echo -e "${RED}[✗]${NC} $1"; exit 1; }

# ============================================================
# WorkBuddy
# ============================================================
install_workbuddy() {
    local target="$HOME/.workbuddy/skills/chen-hansheng-wisdom"
    mkdir -p "$target"
    cp "${REPO_ROOT}/SKILL.md" "${target}/SKILL.md"
    cp -R "${REPO_ROOT}/references" "${target}/"
    log "WorkBuddy 安装完成 → ~/.workbuddy/skills/chen-hansheng-wisdom/"
    warn "请重启 WorkBuddy 使技能生效"
}

# ============================================================
# Claude Code (Agent Skills 标准)
# ============================================================
install_claude_code() {
    local target="$HOME/.claude/skills/chen-hansheng-wisdom"
    mkdir -p "$target"
    cp "${REPO_ROOT}/configs/claude-code/SKILL.md" "${target}/SKILL.md"
    cp -R "${REPO_ROOT}/references" "${target}/"
    log "Claude Code 安装完成 → ~/.claude/skills/chen-hansheng-wisdom/"
    info "使用方式: 输入 /chen-hansheng-wisdom 或让 Claude 自动触发"
}

# ============================================================
# Cursor (.mdc 规则)
# ============================================================
install_cursor() {
    local target=".cursor/rules"
    mkdir -p "$target"
    cp "${REPO_ROOT}/configs/cursor/chen-hansheng-wisdom.mdc" "${target}/"
    log "Cursor 规则已安装 → ./.cursor/rules/chen-hansheng-wisdom.mdc"
    warn "请在 Cursor 中打开规则面板确认已启用 (Rules > Enable)"
}

# ============================================================
# OpenCode (AGENTS.md)
# ============================================================
install_opencode() {
    if [ ! -f "AGENTS.md" ]; then
        cp "${REPO_ROOT}/configs/opencode/AGENTS.md" "./AGENTS.md"
        log "OpenCode 已安装 → ./AGENTS.md"
    else
        warn "已存在 AGENTS.md，请手动合并 configs/opencode/AGENTS.md"
    fi
    info "全局安装可选: mkdir -p ~/.config/opencode && cp configs/opencode/AGENTS.md ~/.config/opencode/"
}

# ============================================================
# Trae (.trae/rules)
# ============================================================
install_trae() {
    local target=".trae/rules"
    mkdir -p "$target"
    cp "${REPO_ROOT}/configs/trae/chen-hansheng-wisdom.md" "${target}/"
    log "Trae 规则已安装 → ./.trae/rules/chen-hansheng-wisdom.md"
    warn "请在 Trae 设置 > 规则 中确认该规则已启用"
}

# ============================================================
# 主逻辑
# ============================================================
usage() {
    echo "用法: bash scripts/install.sh [选项]"
    echo "  --workbuddy      安装到 WorkBuddy"
    echo "  --claude-code    安装到 Claude Code"
    echo "  --cursor         安装到 Cursor"
    echo "  --opencode       安装到 OpenCode"
    echo "  --trae           安装到 Trae"
    echo "  --all            全部安装"
    echo "  --help           显示帮助"
}

if [ $# -eq 0 ]; then
    usage
    exit 1
fi

for arg in "$@"; do
    case "$arg" in
        --workbuddy)     install_workbuddy ;;
        --claude-code)   install_claude_code ;;
        --cursor)        install_cursor ;;
        --opencode)      install_opencode ;;
        --trae)          install_trae ;;
        --all)
            install_workbuddy
            install_claude_code
            install_cursor
            install_opencode
            install_trae
            ;;
        --help|-h)       usage; exit 0 ;;
        *)               warn "未知选项: $arg"; usage; exit 1 ;;
    esac
done

echo ""
log "安装流程完成！重启对应工具后即可生效。"
