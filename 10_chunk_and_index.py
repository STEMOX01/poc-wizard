

Och för `00_setup.sh`:

```bash
cat > 00_setup.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail
# TODO: fyll på med APT, conda, pip-install etc
echo "Här kommer setup-steget"
