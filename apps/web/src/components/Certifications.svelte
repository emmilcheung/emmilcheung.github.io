<script lang="ts">
  interface Certification {
    icon: string;
    name: string;
    issuer: string;
    issuerUrl?: string;
    date: string;
  }

  const certifications: Certification[] = [
    {
      icon: "AWS",
      name: "AWS Certified Developer – Associate",
      issuer: "Amazon Web Services Training and Certification",
      issuerUrl: "https://www.credly.com/badges/5c8c259d-c1d2-49e7-99cf-756c7336c9e0/public_url",
      date: "Oct 2025"
    }
  ];
</script>

<section id="certifications" class="py-20 px-4 bg-gradient-to-br from-orange-50 via-amber-50 to-yellow-50 dark:from-slate-900 dark:via-slate-800 dark:to-slate-900">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <div class="handwriting text-2xl text-amber-600 dark:text-amber-400 mb-2">Achievements</div>
      <h2 class="text-4xl md:text-5xl font-bold text-slate-800 dark:text-slate-100">
        Certifications
      </h2>
    </div>
    
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      {#each certifications as cert}
        <div class="bg-white dark:bg-slate-800 rounded-3xl p-8 hover:shadow-xl transition-all duration-300 hover:-translate-y-2 border-2 border-amber-100 dark:border-slate-700 relative overflow-hidden group">
          <!-- Decorative gradient -->
          <div class="absolute inset-0 bg-gradient-to-br from-amber-100/0 via-amber-100/30 to-orange-100/50 dark:from-amber-900/0 dark:via-amber-900/10 dark:to-orange-900/20 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          
          <div class="relative z-10">
            <div class="inline-block px-4 py-2 bg-amber-500 text-white font-bold rounded-lg mb-4 text-sm">{cert.icon}</div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3 leading-tight">{cert.name}</h3>
            <p class="text-slate-600 dark:text-slate-400 mb-2 text-sm">
              {#if cert.issuerUrl}
                <a href={cert.issuerUrl} target="_blank" rel="noopener noreferrer" class="hover:text-amber-600 dark:hover:text-amber-400 underline decoration-2 underline-offset-2">
                  {cert.issuer}
                </a>
              {:else}
                {cert.issuer}
              {/if}
            </p>
            <div class="inline-block px-3 py-1 bg-amber-100 dark:bg-amber-900/30 rounded-full">
              <p class="text-amber-800 dark:text-amber-300 font-semibold text-sm">{cert.date}</p>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
