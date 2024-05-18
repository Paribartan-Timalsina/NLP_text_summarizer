// TextMaster.js
import React, { useState } from 'react';
import './textmaster.css';
import axios from 'axios';

function TextMaster() {
    const [inputText, setInputText] = useState( "The Mustang, an iconic American muscle car, embodies the spirit of freedom and adventure on the open road. Since its debut in 1964, this legendary vehicle has captured the hearts of enthusiasts worldwide with its sleek design, powerful performance, and unmistakable roar. With its distinctive horse emblem galloping proudly across its grille, the Mustang symbolizes power, agility, and timeless style. From its origins as a revolutionary 'pony car' to its evolution into a symbol of automotive excellence, the Mustang continues to inspire generations of drivers to chase their dreams and embrace the thrill of the ride. Whether tearing up the asphalt of a racetrack or cruising along scenic highways, the Mustang remains an enduring symbol of American automotive ingenuity and passion.");
    const [outputText, setOutputText] = useState('');
    const [loading, setLoading] = useState(false);

    const handleInputChange = (e) => {
        setInputText(e.target.value);
    };

    const handleParaphrase = async () => {
        setLoading(true);
        try {
            const response = await axios.post("http://localhost:8000/summarize", {
                text: inputText
            });
            setOutputText(response.data.summary);
        } catch (error) {
            console.error("There was an error processing the request!", error);
        } finally {
            setLoading(false);
        }
    };

    const countWords = (text) => {
        const words = text.trim().split(/\s+/);
        return words.length;
    };

    const maxWords = 600;

    return (
        <>
            {!loading && (
                <div className="text-master-container">
                    <div className="textmaster-text">TextMaster</div>
                    <div className="main-content">
                        <div className="input-box">
                            <h2>Enter Text</h2>
                            <textarea
                                value={inputText}
                                onChange={handleInputChange}
                                placeholder="Enter your text here..."
                                className="text-area"
                            />
                            <div className='bottomoptions'>
                                <div className="word-count"> Words: {countWords(inputText)}/{maxWords}</div>
                                <button className='uploadPDF'>Upload PDF</button>
                            </div>
                        </div>
                        <div className="output-box">
                            <h2>Summarized Text</h2>
                            <p className="summarized-text">{outputText}</p>
                            <div className="word-count">{countWords(outputText)}/{maxWords}</div>
                        </div>
                    </div>
                    <button onClick={handleParaphrase} className="paraphrase-button">
                        Summarize
                    </button>
                </div>
            )}
            {loading && <h1>Loading...</h1>}
        </>
    );
}

export default TextMaster;
