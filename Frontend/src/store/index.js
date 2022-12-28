import Vue from 'vue';
import Vuex from 'vuex';
import visStore from './modules/visStore'

Vue.use(Vuex);

export default new Vuex.Store ({
    modules: {visStore},
    strict: false
})