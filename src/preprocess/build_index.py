#!/usr/bin/env python3
import argparse, pickle, pathlib, re

def build_index(img_root, report_root, exts=("jpg","jpeg","png")):
    img_root, report_root = pathlib.Path(img_root), pathlib.Path(report_root)
    id_pat = re.compile(r"(s\d{8})")         # 스터디 ID 패턴  ex) s56699142
    index, miss_img, miss_rpt = [], 0, 0

    for img in img_root.rglob("*"):
        if img.suffix[1:].lower() not in exts:
            continue                         # jpg/png 외 무시(index.html 등)
        m = id_pat.search(str(img))
        if not m:                            # 스터디 ID 못 찾으면 skip
            continue
        sid = m.group(1)
        # ── 해당 스터디 리포트(.txt) 찾기 : 보고서 루트 전체 재귀 탐색
        rpt_hits = list(report_root.rglob(f"{sid}.txt"))
        if not rpt_hits:
            miss_rpt += 1
            continue
        index.append({"study_id": sid,
                      "image": str(img),
                      "report": str(rpt_hits[0])})

    print(f"✓ paired  {len(index):,}  image–report samples "
          f"(skip img:{miss_rpt:,})")
    return index

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--img_dir",    required=True)
    ap.add_argument("--report_dir", required=True)
    ap.add_argument("--out",        required=True)
    args = ap.parse_args()

    idx = build_index(args.img_dir, args.report_dir)
    pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    pickle.dump(idx, open(args.out, "wb"))
    print("→ saved:", args.out)

if __name__ == "__main__":
    main()
