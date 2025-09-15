"use client";

import { useState } from "react";

interface ApiResponse {
  message?: string;
  error?: string;
  data?: {
    data: {
      email: "jguilhermeempresarial@outlook.com";
      message: "Curr\u00edculo criado com sucesso!";
      nome_candidato: "JO\u00c3O GUILHERME";
    };
    message: "Curr\u00edculo gerado com sucesso!";
  };
}

export default function Home() {
  const [jobDescription, setJobDescription] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [response, setResponse] = useState<ApiResponse | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setJobDescription(e.target.value);
  };

  const cleanJobDescription = (text: string): string => {
    return text
      .trim() // Remove espaços do início e fim
      .replace(/\n+/g, ' ') // Substitui quebras de linha por espaços
      .replace(/\s+/g, ' ') // Substitui múltiplos espaços por um único espaço
      .trim(); // Remove espaços extras que possam ter sobrado
  };

  const validateInput = (): boolean => {
    return jobDescription.trim().length > 0;
  };

  const sendRequest = async (): Promise<ApiResponse> => {
    const response = await fetch("http://localhost:5000/api/generate-resume", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        descricao_vaga: cleanJobDescription(jobDescription),
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateInput()) {
      setResponse({ error: "Por favor, insira uma descrição da vaga." });
      return;
    }

    setIsLoading(true);
    setResponse(null);

    try {
      const result = await sendRequest();
      setResponse(result);
    } catch (error) {
      setResponse({
        error: `Erro ao processar requisição: ${
          error instanceof Error ? error.message : "Erro desconhecido"
        }`,
      });
    } finally {
      setIsLoading(false);
    }
  };

  const resetForm = () => {
    setJobDescription("");
    setResponse(null);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-2xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            Gerador de Currículo Personalizado
          </h1>
          <p className="text-gray-600">
            Cole a descrição da vaga abaixo para gerar um currículo
            personalizado
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label
              htmlFor="jobDescription"
              className="block text-sm font-medium text-gray-700 mb-2"
            >
              Descrição da Vaga
            </label>
            <textarea
              id="jobDescription"
              value={jobDescription}
              onChange={handleInputChange}
              placeholder="Cole aqui a descrição completa da vaga..."
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-vertical min-h-[200px]"
              disabled={isLoading}
            />
          </div>

          <div className="flex gap-4">
            <button
              type="submit"
              disabled={isLoading || !jobDescription.trim()}
              className="flex-1 bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              {isLoading ? "Processando..." : "Gerar Currículo"}
            </button>

            <button
              type="button"
              onClick={resetForm}
              disabled={isLoading}
              className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              Limpar
            </button>
          </div>
        </form>

        {response && (
          <div className="mt-6 p-4 rounded-md">
            {response.error ? (
              <div className="bg-red-50 border border-red-200 rounded-md p-4">
                <div className="flex">
                  <div className="ml-3">
                    <h3 className="text-sm font-medium text-red-800">Erro</h3>
                    <div className="mt-2 text-sm text-red-700">
                      {response.error}
                    </div>
                  </div>
                </div>
              </div>
            ) : (
              <div className="bg-green-50 border border-green-200 rounded-md p-4">
                <div className="flex">
                  <div className="ml-3">
                    <h3 className="text-sm font-medium text-green-800">
                      Sucesso
                    </h3>
                    <div className="mt-2 text-sm text-green-700">
                      {response.message}
                    </div>
                    {response.data && (
                      <div className="mt-2 text-sm text-green-600">
                        <pre className="whitespace-pre-wrap bg-green-100 p-2 rounded text-xs">
                          {JSON.stringify(response.data, null, 2)}
                        </pre>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
