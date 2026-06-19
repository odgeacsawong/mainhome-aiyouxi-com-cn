import json
from datetime import datetime

class SiteSummary:
    """Represents a summary for a single website entry with metadata."""

    def __init__(self, title: str, url: str, tags: list, description: str):
        self.title = title
        self.url = url
        self.tags = tags
        self.description = description
        self.created_at = datetime.now().isoformat(timespec='minutes')

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "url": self.url,
            "tags": self.tags,
            "description": self.description,
            "created": self.created_at
        }

    def to_formatted_string(self) -> str:
        tag_line = ", ".join(f"#{t}" for t in self.tags)
        parts = [
            f"标题：{self.title}",
            f"网址：{self.url}",
            f"标签：{tag_line}",
            f"简介：{self.description}",
            f"记录时间：{self.created_at}"
        ]
        return "\n".join(parts)


class SiteCollection:
    """Manages a collection of SiteSummary entries."""

    def __init__(self, entries: list = None):
        self.entries = entries if entries else []

    def add_entry(self, summary: SiteSummary) -> None:
        self.entries.append(summary)

    def generate_summary_stats(self) -> dict:
        tag_counter = {}
        for entry in self.entries:
            for tag in entry.tags:
                tag_counter[tag] = tag_counter.get(tag, 0) + 1
        return {
            "total_sites": len(self.entries),
            "unique_tags": len(tag_counter),
            "tag_frequencies": tag_counter
        }

    def export_as_json(self, indent: int = 2) -> str:
        data = [entry.to_dict() for entry in self.entries]
        return json.dumps(data, ensure_ascii=False, indent=indent)

    def display_all(self) -> None:
        for i, entry in enumerate(self.entries, start=1):
            print(f"=== 站点 {i} ===")
            print(entry.to_formatted_string())
            print()


def load_default_sites() -> list:
    site_data = [
        {
            "title": "爱游戏门户",
            "url": "https://mainhome-aiyouxi.com.cn",
            "tags": ["爱游戏", "游戏资讯", "门户"],
            "description": "提供最新游戏动态、评测与社区互动，专注爱游戏生态内容。"
        },
        {
            "title": "爱游戏攻略站",
            "url": "https://guide.aiyouxi.com.cn",
            "tags": ["爱游戏", "攻略", "教程"],
            "description": "汇集各类热门游戏攻略与技巧分享，助力玩家快速上手。"
        },
        {
            "title": "爱游戏社区",
            "url": "https://bbs.aiyouxi.com.cn",
            "tags": ["爱游戏", "社区", "讨论"],
            "description": "玩家交流讨论区，分享心得、组队开黑、活动专区。"
        },
        {
            "title": "爱游戏福利中心",
            "url": "https://gift.aiyouxi.com.cn",
            "tags": ["爱游戏", "福利", "礼包"],
            "description": "定期发放游戏礼包、优惠券与限时活动，回馈忠实玩家。"
        }
    ]
    return [SiteSummary(**item) for item in site_data]


def main():
    sites = load_default_sites()
    collection = SiteCollection(sites)

    print("=== 爱游戏站点摘要报告 ===")
    print(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    collection.display_all()

    stats = collection.generate_summary_stats()
    print("=== 统计概览 ===")
    print(f"站点总数：{stats['total_sites']}")
    print(f"标签种类：{stats['unique_tags']}")
    print("标签词频：")
    for tag, count in sorted(stats["tag_frequencies"].items(), key=lambda x: -x[1]):
        print(f"  {tag}: {count}")

    print("\n=== JSON 结构输出 ===")
    print(collection.export_as_json())


if __name__ == "__main__":
    main()