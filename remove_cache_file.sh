find . -depth 1 -type d -name '__pycache__' -exec rm -rf {} \;
find . -depth 1 -type d -name '.pytest_cache' -exec rm -rf {} \;
