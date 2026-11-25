# 旧鞋整备抽检与学校成双交接

每条抽检记录涉及单只鞋。P 表示左脚，Q 表示右脚。抽样框的袋数和未拆件数分别记录。尺码为欧码。

## 资料

CSV 样例为合成记录，使用 UTF-8，首行为字段名。多值用竖线分隔，空单元格表示来源未填。记录日期和业务生效日期各有含义。

- lots.csv 的字段为 lot、origin、bags、unopened_shoes、clean_job、process_day。
- sample.csv 的字段为 item、lot、bag、selection、side、size、condition、known_on。
- counts.csv 的字段为 record、lot、side、size、usable、as_of、revision。
- release.csv 的字段为 release、job、lot、max_pairs、reported、state。
- schools.csv 的字段为 school、ordered_size、acceptable_sizes、min_pack、requested、deadline、allowed_jobs。
- travel.csv 的字段为 truck、date、cap_pairs、stops。
- receipts.csv 的字段为 delivery、school、truck、lot、pairs、size、at、status。
- sampling_frames.csv 的字段为 stratum、lot、eligible_bags、random_bags、revision。

## 运行资料检查

在项目根目录使用 Python 3.11 或更高版本。依赖仅为标准库。

~~~sh
python3 -m compileall -q tests
python3 -m unittest discover -s tests -v
~~~
