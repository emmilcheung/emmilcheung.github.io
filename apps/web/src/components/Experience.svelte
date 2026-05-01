<script lang="ts">
  interface Achievement {
    icon: string;
    title: string;
    description: string;
    descriptionHtml?: string; // HTML version with links
  }

  interface Experience {
    title: string;
    company: string;
    companyUrl?: string;
    location: string;
    period: string;
    techStack: string[];
    achievements: Achievement[];
  }

  const experiences: Experience[] = [
    {
      title: "Programmer",
      company: "Zensis Limited",
      companyUrl: "https://www.zensis.com/",
      location: "Hong Kong",
      period: "Aug 2021 - Aug 2025",
      techStack: ["NodeJS", "Java", "Python", "React.js", "MongoDB", "Redis", "Docker", "AWS"],
      achievements: [
        {
          icon: "☁️",
          title: "Cloud Native Development",
          description: "Served as a key contributor and maintainer for cloud native applications throughout the full Software Development Life Cycle (SDLC), encompassing requirement analysis, technical planning, development, deployment and documentation"
        },
        {
          icon: "🚀",
          title: "CI/CD & DevOps",
          description: "Established GitOps and CI/CD workflows for both internal and client projects by streamlining development processes through GitLab CI, Docker, Terraform and Jenkins, achieving 50%+ reduction in time required to introduce new projects and stages"
        },
        {
          icon: "🧪",
          title: "System Architecture",
          description: "Facilitated the in-house system revamp by Object-Orientated Design and Dependency Injection (DI) framework in TypeScript with comprehensive unit and integration tests, achieving a 70%+ increase in code coverage and reduction in bugs report"
        },
        {
          icon: "📱",
          title: "Enterprise Solutions",
          description: "Designed and developed backend services and APIs in NodeJS for the staff communication application of Wilson Group utilizing service-oriented architecture (SOA), role-based access control (RBAC) and Terraform on AWS and MongoDB Atlas, facilitating on-job training, events and information delivery within 5000+ active employees",
          descriptionHtml: 'Designed and developed backend services and APIs in NodeJS for the <a href="https://www.zensis.com/portfolio/wilson-group/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">staff communication application</a> of Wilson Group utilizing service-oriented architecture (SOA), role-based access control (RBAC) and Terraform on AWS and MongoDB Atlas, facilitating on-job training, events and information delivery within <strong>5000+ active employees</strong>'
        },
        {
          icon: "⚡",
          title: "Serverless Architecture",
          description: "Managed an event-driven system and organizer panel of a real-time trail running event application under AWS serverless architecture (AWS Lambda, SQS, AppSync, S3, CloudWatch), GraphQL and Next.js, supporting 20+ public events annually",
          descriptionHtml: 'Managed an event-driven system and organizer panel of a real-time <a href="https://www.zensis.com/portfolio/trailme/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">trail running event application</a> under AWS serverless architecture (AWS Lambda, SQS, AppSync, S3, CloudWatch), GraphQL and Next.js, supporting <strong>20+ public events annually</strong>'
        },
        {
          icon: "🎨",
          title: "Frontend Development",
          description: "Built front-end web applications, widgets, and UI components under React.js and modern JavaScript best practices for clients across diverse industries including 9GAG, ViuTV, Makealive, Open Up, GO PARK Sports, and government",
          descriptionHtml: 'Built front-end web applications, widgets, and UI components under React.js and modern JavaScript best practices for clients across diverse industries including <a href="https://9gag.com/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">9GAG</a>, <a href="https://www.zensis.com/portfolio/viutv/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">ViuTV</a>, <a href="https://makealive.com/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">Makealive</a>, <a href="https://www.zensis.com/portfolio/openup/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">Open Up</a>, <a href="https://www.zensis.com/portfolio/go-park-sports/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">GO PARK Sports</a>, and <a href="https://www.zensis.com/portfolio/ipdnofakes/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">government</a>'
        },
        {
          icon: "🤖",
          title: "AI Integration",
          description: "Built in-house product, Chatsquare (Q&A Chatbot, Admin panel), and feedback system with Next.js, LangChain and Redis",
          descriptionHtml: 'Built in-house product, <a href="https://www.chatsquare.ai/" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300 underline">Chatsquare</a> (Q&A Chatbot, Admin panel), and feedback system with Next.js, LangChain and Redis'
        },
        {
          icon: "🔧",
          title: "Legacy Maintenance",
          description: "Participated in maintenance and support routine for legacy systems in Vert.x 3 (Java), Flask (Python) and NodeJS"
        }
      ]
    },
    {
      title: "Web App Development Intern",
      company: "ponte+",
      companyUrl: "https://hk.linkedin.com/company/ponteplus",
      location: "Hong Kong",
      period: "Aug 2020 - Oct 2020",
      techStack: ["NodeJS", "React.js", "Firebase", "Adobe XD"],
      achievements: [
        {
          icon: "📲",
          title: "PWA Development",
          description: "Developed a mobile-first Progressive Web App (PWA) focused on performing art events from scratch and delivered to beta"
        },
        {
          icon: "🤝",
          title: "Collaboration",
          description: "Participated in weekly meetings with director, supervisor and UI/UX Designer on business and development direction"
        }
      ]
    },
    {
      title: "Part-time Customer Service Assistant",
      company: "The Commercial Press (HK) Ltd",
      companyUrl: "https://www.commercialpress.com.hk/ww/index.html",
      location: "Hong Kong",
      period: "Feb 2017 - Oct 2020",
      techStack: [],
      achievements: [
        {
          icon: "🏪",
          title: "Customer Operations",
          description: "Supported daily store operations, customer assistance, product purchases and inter-shop logistic arrangement"
        },
        {
            icon: "📚",
            title: "Tool Development",
            description: "Built a book search web application with React.js and Flask(python) for internal use to facilitate book search and inventory check"
        },
        {
            icon: "📱",
            title: "Order Communication Automation",
            description: "Enhanced message delivery on order status updates to customers by developing automated VBA scripts integrated with WhatsApp Business API"
        }
      ]
    }
  ];
</script>

<section id="experience" class="py-20 px-4 bg-white dark:bg-slate-900">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <div class="handwriting text-2xl text-amber-600 dark:text-amber-400 mb-2">My journey</div>
      <h2 class="text-4xl md:text-5xl font-bold text-slate-800 dark:text-slate-100">
        Work Experience
      </h2>
    </div>
    
    <div class="space-y-8">
      {#each experiences as exp, i}
        <div class="bg-gradient-to-br from-amber-50 to-orange-50 dark:from-slate-800 dark:to-slate-800/50 rounded-3xl p-8 hover:shadow-xl transition-all duration-300 border-2 border-amber-100 dark:border-slate-700 relative overflow-hidden" style="animation-delay: {i * 0.1}s">
          <!-- Decorative element -->
          <div class="absolute top-0 right-0 w-32 h-32 bg-amber-200/20 dark:bg-amber-900/10 rounded-full -mr-16 -mt-16"></div>
          
          <div class="flex flex-col md:flex-row md:items-start md:justify-between mb-6 relative z-10">
            <div class="mb-4 md:mb-0">
              <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">{exp.title}</h3>
              <p class="text-lg text-amber-700 dark:text-amber-400 font-medium">
                {#if exp.companyUrl}
                  <a href={exp.companyUrl} target="_blank" rel="noopener noreferrer" class="hover:text-amber-800 dark:hover:text-amber-300 underline decoration-2 underline-offset-2">
                    {exp.company}
                  </a>
                {:else}
                  {exp.company}
                {/if}
                <span class="text-slate-600 dark:text-slate-400"> · {exp.location}</span>
              </p>
            </div>
            <div class="inline-block px-4 py-1.5 bg-white/70 dark:bg-slate-700/70 backdrop-blur-sm rounded-full text-slate-600 dark:text-slate-300 font-medium text-sm">
              {exp.period}
            </div>
          </div>
          
          {#if exp.techStack.length > 0}
            <div class="mb-6 p-4 bg-white/60 dark:bg-slate-700/50 rounded-2xl border border-amber-200 dark:border-slate-600 backdrop-blur-sm relative z-10">
              <p class="font-semibold text-slate-700 dark:text-slate-300 mb-3 uppercase text-xs tracking-wider">
                Technologies Used
              </p>
              <div class="flex flex-wrap gap-2">
                {#each exp.techStack as tech}
                  <span class="px-3 py-1.5 bg-amber-100 dark:bg-amber-900/30 text-amber-900 dark:text-amber-300 rounded-full text-sm font-medium border border-amber-200 dark:border-amber-800">
                    {tech}
                  </span>
                {/each}
              </div>
            </div>
          {/if}
          
          <div class="space-y-5 relative z-10">
            {#each exp.achievements as achievement}
              <div class="border-l-2 border-amber-400 pl-4">
                <div class="flex-1">
                  <h4 class="font-bold text-slate-900 dark:text-white mb-2">{achievement.title}</h4>
                  {#if achievement.descriptionHtml}
                    <p class="text-slate-700 dark:text-slate-300 leading-relaxed">{@html achievement.descriptionHtml}</p>
                  {:else}
                    <p class="text-slate-700 dark:text-slate-300 leading-relaxed">{achievement.description}</p>
                  {/if}
                </div>
              </div>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
