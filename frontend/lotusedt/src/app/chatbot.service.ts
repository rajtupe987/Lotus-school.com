import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root',
})
export class ChatbotService {
    private apiUrl = 'https://api.openai.com/v1/chat/completions';
  private apiKey = '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';
  private modelName = 'gpt-3.5-turbo';

  constructor() { }

  async getBotResponse(userInput: string): Promise<string> {
    const params = {
      model: this.modelName,
      messages: [
        {
          role: 'system',
          content: 'You are a chatbot that provides information about Lotus school which is our website which is for students learning perpose there are 5 departments Biology, Mathtamatics, Geography,Computer Science,Geography and Instructors as Varun bhat,Yoges bhat,Ankush chimnani, mohshin students will be able to enroll with an any course and can get better student experianc.Now on the basis of this only you have to give the answer in just one line answer should not go beyound one like and if any queation is asked irrelavent to this say "Ask me queation regarding Lotus school"  '
        },
        {
          role: 'user',
          content: userInput
        }
      ]
    };

    try {
      const response = await axios.post(
        this.apiUrl,
        params,
        {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${this.apiKey}`
          }
        }
      );

      return response.data.choices[0].message.content;
    } catch (error:any) {
      console.error('Error fetching response from the API:', error.response?.data || error.message);
      return 'An error occurred while processing your request.';
    }
  }
}
