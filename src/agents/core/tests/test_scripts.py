"""测试脚本的可调用性"""

import os
import subprocess

import pytest


def test_run_agent_script_exists():
    """测试run_agent.sh脚本是否存在"""
    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts", "run_agent.sh")
    assert os.path.exists(script_path), f"脚本不存在: {script_path}"


@pytest.mark.skip(reason="需要在实际环境中运行，CI环境可能没有uv")
def test_run_agent_script_help():
    """测试run_agent.sh脚本是否可以正常执行"""
    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts", "run_agent.sh")

    # 添加可执行权限
    os.chmod(script_path, 0o755)

    # 运行脚本，传入--help参数
    process = subprocess.run(
        ["bash", script_path, "--help"],
        capture_output=True,
        text=True
    )

    # 检查退出码
    assert process.returncode == 0, f"脚本执行失败: {process.stderr}"
