<script lang="ts">
  interface SkillCategory {
    icon: string;
    title: string;
    skills: string[];
  }

  const skillCategories: SkillCategory[] = [
    {
      icon: "</>",
      title: "Programming Languages",
      skills: ["Java", "JavaScript", "TypeScript", "Python", "Golang", "SQL", "HTML", "CSS"]
    },
    {
      icon: "{ }",
      title: "Frameworks & Libraries",
      skills: ["Express.js", "NestJS", "ReactJS", "Next.js", "Jest", "Mocha", "Playwright", "Flask", "Spring Boot", "gRPC"]
    },
    {
      icon: "[ ]",
      title: "Tools & Platforms",
      skills: ["Git", "GitLab", "Docker", "Kubernetes", "Terraform", "MongoDB", "PostgreSQL", "Redis", "AWS", "GCP", "Firebase"]
    }
  ];
</script>

<section id="skills" class="py-20 px-4 bg-white dark:bg-slate-900">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <div class="handwriting text-2xl text-amber-600 dark:text-amber-400 mb-2">What I work with</div>
      <h2 class="text-4xl md:text-5xl font-bold text-slate-800 dark:text-slate-100">
        Skills & Tools
      </h2>
    </div>
    
    <div class="grid md:grid-cols-3 gap-8">
      {#each skillCategories as category, i}
        <div class="bg-gradient-to-br from-amber-50 to-orange-50 dark:from-slate-800 dark:to-slate-800/50 rounded-3xl p-8 hover:shadow-xl transition-all duration-300 border-2 border-amber-100 dark:border-slate-700 hover:-translate-y-2 relative overflow-hidden" style="animation-delay: {i * 0.1}s">
          <!-- Decorative element -->
          <div class="absolute -bottom-6 -right-6 text-9xl font-mono opacity-5 text-amber-600 dark:text-amber-400">{category.icon}</div>
          
          <div class="mb-6 relative z-10">
            <div class="text-2xl font-mono text-amber-600 dark:text-amber-400 mb-2">{category.icon}</div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white">{category.title}</h3>
          </div>
          
          <div class="flex flex-wrap gap-2 relative z-10">
            {#each category.skills as skill}
              <span class="px-3 py-2 bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-200 rounded-xl text-sm font-medium border border-amber-200 dark:border-slate-600 hover:bg-amber-100 dark:hover:bg-slate-600 transition-colors">
                {skill}
              </span>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
