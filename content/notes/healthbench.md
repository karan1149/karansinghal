+++ 
draft = false

title = "HealthBench"
description = "HealthBench: Evaluating Large Language Models Towards Improved Human Health"

tags = ["tweets", "work"]
categories = []
series = []

date = 2025-05-12T13:54:40-07:00
hideDate = false
hideCategories = true
hideTags = true
hideReadingTime = true
hideShareButtons = true
katex = false
+++

I'm proud to share [HealthBench](https://openai.com/index/healthbench/), an open-source benchmark from our Health AI team at OpenAI that measures LLM performance and safety across 5,000 realistic health conversations.

Unlike previous narrow benchmarks, HealthBench enables meaningful open-ended evaluation through 48,562 unique physician-written rubric criteria spanning several health contexts (e.g., emergencies, global health) and behavioral dimensions (e.g., accuracy, instruction following, communication).

{{< image fallback_path="/images/healthbench/healthbench_1.jpeg" caption="HealthBench overview. Model responses are graded via physician-written rubrics." max_width="100%" >}}

We built HealthBench over the last year, working with 262 physicians across 26 specialties with practice experience in 60 countries (below), across selecting focus areas, generating relevant and difficult examples, annotating examples, and validating every step along the way.

{{< image fallback_path="/images/healthbench/healthbench_2.jpeg" caption="Physician cohort countries of practice." max_width="100%" >}}

### Evaluation results

Using HealthBench, we see that our Apr 2025 models define a new frontier of performance at cost, with GPT-4.1 nano outperforming GPT-4o (Aug 2024), despite being 25x cheaper. The difference between o3 and GPT-4o (.28) is greater than between GPT-4o and GPT-3.5 Turbo (.16).

{{< image fallback_path="/images/healthbench/healthbench_3.jpeg" caption="New models push the performance-cost frontier." max_width="70%" >}}

We compare our models to those of other model providers, stratified by focus areas. o3 performs best overall but headroom remains.

{{< image fallback_path="/images/healthbench/healthbench_4.jpeg" caption="HealthBench performance across themes for different models." max_width="100%" >}}

Reliability is critical in healthcare–one bad response can outweigh many good ones. We measure worst-case performance at k samples across HealthBench, and find that o3 has more than twice the worst-case score at 16 samples compared to GPT-4o.

{{< image fallback_path="/images/healthbench/healthbench_5.jpeg" caption="Our recent models are also more reliable." max_width="100%" >}}

As a bonus, we introduce two additional members of the HealthBench family: HealthBench Hard and HealthBench Consensus, which are designed to be especially difficult and physician-validated, respectively. The top model scores just 32% on HealthBench Hard, making it a worthy target for next-generation models.

{{< image fallback_path="/images/healthbench/healthbench_6.jpeg" caption="HealthBench Hard is designed to be an especially difficult subset of HealthBench." max_width="100%" >}}

We believe health evaluations should be trustworthy. We measured agreement of our model-based grading against physician grading on HealthBench Consensus (to measure trustworthiness compared to physicians), and found that models matched a median physician for 6/7 areas, indicating that HealthBench scores correspond to physician judgment.

{{< image fallback_path="/images/healthbench/healthbench_7.jpeg" caption="Model-based grading matches or exceeds the median physician in most areas." max_width="100%" >}}

We share more results in the [paper](https://arxiv.org/pdf/2505.08775), including a physician baseline study.

### Why we did this

We designed HealthBench for two audiences:

- AI research community: to shape shared standards and incentivize models that benefit humanity
- Healthcare: to provide high-quality evidence, towards a better understanding of current and future use cases and limitations

We hope that the release of this work guides AI progress towards improved human health.

This work would not have been possible without the unrelenting care and hard work of many, especially our co-authors and 262 members of our physician cohort. Those who wished to be named are listed in the [blog](https://openai.com/index/healthbench/) and [paper](https://arxiv.org/pdf/2505.08775). 

{{< image fallback_path="/images/healthbench/healthbench_8.png" caption="Kudos to the team!" max_width="100%" >}}

If you're interested in contributing to our team, we are hiring [Research Scientists / Engineers](https://openai.com/careers/research-engineer-scientist-health-ai/) and [Software Engineers](https://openai.com/careers/software-engineer-healthcare/)!


Links: [[Blog Post]](https://openai.com/index/healthbench/) [[Paper]](https://arxiv.org/pdf/2505.08775) [[Code]](https://github.com/openai/simple-evals)
[[Tweet]](https://x.com/thekaransinghal/status/1921996747947311587) [[LinkedIn]](https://www.linkedin.com/posts/karan1149_introducing-healthbench-activity-7327768726496305152-L8OW?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAOzqSIBC-_-GGIxm0-8USf1NmaKbKbzTpk)

