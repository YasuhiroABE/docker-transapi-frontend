<template>
  <div class="translation">
    <a target="_blank" href="http://localhost:8983/">Open Solr Console</a>
    <br />
    <textarea class="input-ja" v-model="text_ja" @keydown.enter="search_api" placeholder="日本語" />
    <textarea class="input-en" v-model="text_en" placeholder="English" />
    <br />
    <button class="button-search" type="button" v-on:click="exec_trans" >翻訳開始</button>
    <button class="button-regist" v-on:click="exec_regist" type="button">手動登録</button>
    <label>再翻訳</label>: <input v-model="is_exec_trans" type="checkbox" v-on:click="clicked_is_exec_trans" /> <p>{{ this.trans_warning }}</p>

    <h2>Ans. of {{ this.text_ja }}</h2>
    <table class="result">
    <thead>
    <tr>
      <th>No.</th>
      <th>日本語</th>
      <th>English</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="(item, index) in info" :key="[item.id,item.translation]" @click="overwrite_jaen_input_field(item.id, item.translation[0])">
      <td>{{ index + 1 }}</td>
      <td>{{ item.id }}</td>
      <td>{{ item.translation[0] }}</td>
    </tr>
    </tbody>
    </table>

    <h2>Translation Result</h2>
    <table class="result">
    <thead>
    <tr>
      <th>No.</th>
      <th>Engine</th>
      <th>日本語</th>
      <th>English</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="(item, index) in trans_result" :key="[item.engine,item.original_text,item.translate_text]" @click="overwrite_jaen_input_field(item.original_text, item.translate_text)">
      <td>{{ index + 1 }}</td>
      <td>{{ item.engine }}</td>
      <td>{{ item.original_text }}</td>
      <td>{{ item.translate_text }}</td>
    </tr>
    </tbody>
    </table>

    <h2>Registration Results</h2>
    <p>{{ results }}</p>

  </div>
</template>

<script>
/* from axios */
import axios from "axios"

export default {
  name: 'Translation',
  props: {
      text_ja: { type: String },
      text_en: { type: String },
      is_exec_trans: { type: Boolean },
      info: { type: String },
      results: { type: String }, 
      trans_result: { type: String },
      trans_warning: { type: String },
  },
  methods: {
    exec_regist() {
       axios
      .post("http://127.0.0.1:8080/dict?ja=" + this.text_ja + "&en=" + this.text_en, '')
      .then(response => (this.results = response));
    },
    exec_trans() {
      this.trans_warning = "";
      if(this.is_exec_trans) {
        axios
          .get("http://127.0.0.1:8080/trans?q=" + this.text_ja )
          .then(response => (this.trans_result = response.data.results));
        this.is_exec_trans = false;
      } else {
        this.trans_warning = "翻訳機能を利用する際はチェックをオンにしてください。";
      }
    },
    search_api() {
      axios
      .get("http://127.0.0.1:8080/dict?q=" + this.text_ja )
      .then(response => (this.info = response.data.response.docs));
    },
    overwrite_jaen_input_field(ja_text, en_text) {
      this.text_ja = ja_text;
      this.text_en = en_text;
    },
    clicked_is_exec_trans() {
      this.trans_warning = "";
    },
  },
}
</script>

<style scoped lang="css">
.input-ja {
  margin: 0;
}

.input-en {
  margin: 0;
  margin: 0;
}

.button-search {
  background: #efeeff;
  margin: 1em;
}

.result {
  margin: 0 auto;
}
</style>
