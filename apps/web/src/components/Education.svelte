<script lang="ts">
  interface EducationDetail {
    label: string;
    value: string;
  }

  interface Education {
    degree: string;
    institution: string;
    institutionUrl?: string;
    period: string;
    details: EducationDetail[];
  }

  const education: Education = {
    degree: "BSc in Computer Science",
    institution: "The Chinese University of Hong Kong (CUHK)",
    institutionUrl: "https://www.cse.cuhk.edu.hk/",
    period: "Sep 2017 - Jul 2021",
    details: [
      {
        label: "Honours",
        value: "Second Class Upper Division"
      },
      {
        label: "Stream",
        value: "Distributed Systems, Networks and Security"
      },
      {
        label: "Minor",
        value: "Japanese Language"
      }
    ]
  };
</script>

<section id="education" class="py-20 px-4 bg-gradient-to-br from-rose-50 via-amber-50 to-orange-50 dark:from-slate-900 dark:via-slate-800 dark:to-slate-900">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <div class="handwriting text-2xl text-amber-600 dark:text-amber-400 mb-2">Where I learned</div>
      <h2 class="text-4xl md:text-5xl font-bold text-slate-800 dark:text-slate-100">
        Education
      </h2>
    </div>
    
    <div class="bg-white dark:bg-slate-800 rounded-3xl shadow-2xl p-10 max-w-4xl mx-auto hover:shadow-2xl transition-all duration-300 border-2 border-amber-100 dark:border-slate-700 relative overflow-hidden">
      <!-- Decorative blobs -->
      <div class="absolute top-0 left-0 w-40 h-40 bg-gradient-to-br from-amber-200/30 to-rose-200/30 dark:from-amber-900/20 dark:to-rose-900/20 rounded-full -ml-20 -mt-20"></div>
      <div class="absolute bottom-0 right-0 w-32 h-32 bg-gradient-to-tl from-orange-200/30 to-amber-200/30 dark:from-orange-900/20 dark:to-amber-900/20 rounded-full -mr-16 -mb-16"></div>
      <div class="flex flex-col md:flex-row md:items-start md:justify-between mb-8 relative z-10">
        <div class="mb-4 md:mb-0">
          <h3 class="text-2xl md:text-3xl font-bold text-slate-900 dark:text-white mb-3">{education.degree}</h3>
          <p class="text-lg text-amber-700 dark:text-amber-400 font-medium">
            {#if education.institutionUrl}
              <a href={education.institutionUrl} target="_blank" rel="noopener noreferrer" class="hover:text-amber-800 dark:hover:text-amber-300 underline decoration-2 underline-offset-2">
                {education.institution}
              </a>
            {:else}
              {education.institution}
            {/if}
          </p>
        </div>
        <div class="inline-block px-4 py-2 bg-amber-100 dark:bg-amber-900/30 rounded-full text-slate-700 dark:text-slate-300 font-medium">
          {education.period}
        </div>
      </div>
      
      <div class="grid md:grid-cols-3 gap-6 mt-8 relative z-10">
        {#each education.details as detail}
          <div class="p-5 bg-gradient-to-br from-white to-amber-50 dark:from-slate-700 dark:to-slate-700/50 rounded-2xl border-2 border-amber-200 dark:border-slate-600 hover:-translate-y-1 transition-transform">
            <p class="font-bold text-slate-900 dark:text-white mb-2 uppercase text-xs tracking-wider text-amber-700 dark:text-amber-400">{detail.label}</p>
            <p class="text-slate-800 dark:text-slate-200 font-medium">{detail.value}</p>
          </div>
        {/each}
      </div>
    </div>
  </div>
</section>
