import {useState} from 'react';

function App() {
  const [value, setValue] = useState("");
  const [result, setResult] = useState("");

  async function postRequest(mode) {
    if (value) {
      const formData = new FormData();
      formData.append("content", value);
      console.log(`http://127.0.0.1:5000/${mode}`);
      try {
        const response = await fetch(`http://127.0.0.1:5000/${mode}`, {
          method: "POST",
          body: formData,
        });
        const response_text = await response.text();
        console.log(response_text);
        setResult(response_text);

      } catch (error) {
        console.log(error);
      }
    
    }
  }

  
  return (
    <div className="text-center">
      <h1 className="text-3xl font-bold">
        Please paste the text or url to the textbox
      </h1>
      <input
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className="block mx-auto border-2 border-gray-300 round-lg placeholder-gray-500 transition-colors duration-300 hover:border-gray-700"
      />
      <button
        onClick={() => postRequest("text")}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Summarize Text
      </button>
      <button
        onClick={() => postRequest("web")}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Summarize Website
      </button>
      <p>{result}</p>
    </div>
  );
}

export default App;
