<script setup>
import { ref } from "vue";

const telaAtiva = ref("home");
const arquivo = ref(null);
const status = ref("");
const estaProcessando = ref(false);

const cardsConversor = [
  { id: "word", titulo: "Word para PDF", icone: "📄", aceita: ".docx,.doc" },
  { id: "excel", titulo: "Excel para PDF", icone: "📊", aceita: ".xlsx,.xls,.ods" },
  { id: "jpg", titulo: "JPG para PDF", icone: "🖼️", aceita: ".jpg,.jpeg,.png" },
];

const aoSelecionarArquivo = (e) => {
  arquivo.value = e.target.files[0];
  status.value = "";
};

const converterArquivo = async (tipoConversao) => {
  if (!arquivo.value) return;
  estaProcessando.value = true;
  status.value = "Convertendo com segurança...";

  const formData = new FormData();
  formData.append("file", arquivo.value);

  try {
    const resposta = await fetch(
      `https://seadoc.duckdns.org/api/convert/${tipoConversao}-to-pdf`,
      { method: "POST", body: formData }
    );
    if (resposta.ok) {
      const blob = await resposta.blob();
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = arquivo.value.name.replace(/\.[^/.]+$/, "") + ".pdf";
      link.click();
      status.value = "✅ Pronto! PDF baixado.";
      arquivo.value = null;
    } else {
      status.value = "❌ Erro na conversão.";
    }
  } catch (erro) {
    status.value = "❌ Erro de conexão.";
  } finally {
    estaProcessando.value = false;
  }
};
</script>

<template>
  <div
    class="min-h-screen bg-[#f4f7f6] text-gray-800 font-sans flex flex-col items-center"
  >
    <header
      class="w-full bg-white border-b-[3px] border-red-700 shadow-sm p-6 mb-10 flex justify-center"
    >
      <div class="flex items-center gap-4 max-w-5xl w-full">
        <img src="/favicon.svg" alt="SC" class="h-12 w-auto" />
        <div>
          <h1 class="text-2xl font-bold text-red-700 m-0 leading-tight">SeaDoc</h1>
          <p class="text-sm text-gray-600 m-0">Conversor Seguro</p>
        </div>
      </div>
    </header>

    <main class="w-full max-w-5xl px-6 flex-grow">
      <section v-if="telaAtiva === 'home'">
        <h2 class="text-center text-gray-600 mb-8 text-xl font-medium">
          Selecione o conversor desejado:
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="card in cardsConversor"
            :key="card.id"
            @click="telaAtiva = card.id"
            class="bg-white p-8 rounded-lg text-center cursor-pointer border border-gray-200 shadow-sm hover:-translate-y-1 hover:border-red-700 hover:shadow-md transition-all"
          >
            <div class="text-6xl mb-4">{{ card.icone }}</div>
            <h3 class="text-red-700 font-bold text-lg mb-1">{{ card.titulo }}</h3>
            <p class="text-sm text-gray-500">Processamento 100% privado.</p>
          </div>
        </div>
      </section>

      <section
        v-else
        class="max-w-xl mx-auto bg-white p-10 rounded-lg shadow-sm border border-gray-200"
      >
        <button
          @click="
            telaAtiva = 'home';
            arquivo = null;
            status = '';
          "
          class="text-red-700 font-bold mb-6 hover:underline flex items-center gap-2"
        >
          ⬅️ Voltar
        </button>

        <div class="flex items-center gap-4 mb-8 border-b border-gray-100 pb-4">
          <span class="text-5xl">{{
            cardsConversor.find((c) => c.id === telaAtiva)?.icone
          }}</span>
          <h2 class="text-2xl font-bold text-gray-800">
            Conversor {{ cardsConversor.find((c) => c.id === telaAtiva)?.titulo }}
          </h2>
        </div>

        <div class="mb-6">
          <input
            type="file"
            :accept="cardsConversor.find((c) => c.id === telaAtiva)?.aceita"
            id="entradaArquivo"
            @change="aoSelecionarArquivo"
            class="hidden"
          />
          <label
            for="entradaArquivo"
            class="block w-full p-10 bg-[#fafafa] border-2 border-dashed border-gray-300 rounded-lg text-center cursor-pointer hover:border-red-700 hover:bg-white transition-colors"
          >
            <span class="text-gray-700 font-medium">{{
              arquivo ? arquivo.name : "Clique para selecionar o arquivo"
            }}</span>
          </label>
        </div>

        <button
          v-if="arquivo"
          @click="converterArquivo(telaAtiva)"
          :disabled="estaProcessando"
          class="w-full bg-red-700 text-white font-bold py-4 rounded-lg hover:bg-red-800 disabled:bg-gray-400 transition-colors text-lg"
        >
          {{ estaProcessando ? "Processando..." : "Converter para PDF" }}
        </button>

        <p class="text-center mt-4 font-bold text-gray-600">{{ status }}</p>
      </section>
    </main>
  </div>
</template>
