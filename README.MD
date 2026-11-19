# Python Port Scanner

A small TCP port scanner written in Python (standard library only), built in three versions.

> For educational use only. Scan only systems you own or have permission to test.

## Versions

| Version | File | Description |
|---------|------|-------------|
| 1 | `scanner_version1.py` | First working scanner. Found port 135 on localhost, but took about 2 min 25 s. |
| 2 | `scanner_version2.py` | Much faster. Found ports 135 and 445 on localhost in 12.46 s. |
| 3 | `scanner_version3.py` | Multithreaded scanner with banner grabbing and a command-line interface. |

## Usage (version 3)

```bash
python scanner_version3.py <host> [-s START] [-e END] [-t THREADS]
```

| Option | Description | Default |
|--------|-------------|---------|
| `-s`, `--start` | First port | `1`|
| `-e`, `--end` | Last port | `1024` |
| `-t`, `--threads` | Number of threads | `100` |

Example:

```bash
python scanner_version3.py 127.0.0.1 -s 1 -e 1000 -t 200
```

## Results

Tested on `127.0.0.1`.

| | Version 1 | Version 2 |
|---|-----------|-----------|
| Open TCP ports | 135 | 135, 445 |
| Scan time | 2 min 25 s | 12.46 s |

Version 2 was about 11.6x faster and found one more open port.

## What I learned

- **Sockets:** opening a TCP connection with `socket`, where `connect_ex()` returns `0` for an open port.
- **Speed:** scanning one port at a time wastes time on timeouts, and running checks in parallel made the scan much faster.
- **Threading:** using `ThreadPoolExecutor` with `max_workers`.
- **Command-line tools:** building a CLI with `argparse`.
- **Banner grabbing:** some services send a banner right away, others need a probe first.