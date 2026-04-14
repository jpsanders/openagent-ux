# openagent-ux installation script for Unix/Linux/macOS

set -e

echo "Installing openagent-ux skills..."

# Create Claude config directory if it doesn't exist
mkdir -p ~/.claude

# Copy the agents folder to Claude config
if [ -d ".agents" ]; then
    cp -r .agents/* ~/.claude/
    echo "✅ Skills copied to ~/.claude/"
else
    echo "⚠️  .agents directory not found. Are you in the right directory?"
    exit 1
fi

# Try to install graphify if available
if command -v graphify &> /dev/null; then
    echo "✅ Graphify already installed"
else
    echo "ℹ️  Install graphify for knowledge graphs: pip install graphifyy"
fi

echo ""
echo "========== INSTALLATION COMPLETE =========="
echo ""
echo "Next steps:"
echo "1. Restart your AI agent"
echo "2. Run /brand to establish your brand identity"
echo "3. Run /build to create your website"
echo ""
echo "Demo app:"
echo "  cd example-app && npm install && npm run dev"
echo ""
echo "For installation help, see README.md"