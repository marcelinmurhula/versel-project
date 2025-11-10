# Create api/deepseek_integration.py
import os
import requests
import json

class DeepSeekAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v1/chat/completions"
    
    def generate_stepwise_logic(self, prompt):
        """Generate step-by-step educational logic for any STEM topic"""
        
        system_prompt = """You are VERSEL - an AI educational video generator. For any STEM prompt, generate:
1. Domain detection (Physics, CS, Chemistry, etc.)
2. Step-by-step educational logic (3-5 key steps)
3. Animation type (2D/Manim or 3D/Blender)
4. Visual style (Braille-dots or Stick-figures)

Format your response as JSON with: domain, steps[], animationEngine, visualStyle"""

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return self._get_fallback_logic(prompt)
        # Create animators/manim_animator.py
from manim import *
import json

class ManimAnimator:
    def __init__(self):
        self.scene_templates = {
            "physics": self.create_physics_animation,
            "computer_science": self.create_cs_animation,
            "chemistry": self.create_chemistry_animation,
            # Add more domains...
        }
    
    def create_physics_animation(self, logic, scene_class):
        """Create physics animations like Falkirk Wheel"""
        steps = logic.get('steps', [])
        
        # Falkirk Wheel animation
        if "wheel" in logic.get('domain', '').lower():
            wheel = Circle(radius=2, color=WHITE, stroke_width=4)
            axle = Dot(radius=0.1, color=YELLOW)
            
            # Create caissons (water bowls)
            caisson1 = Rectangle(height=1.5, width=1, color=BLUE, fill_opacity=0.5)
            caisson1.move_to(wheel.point_at_angle(45 * DEGREES))
            
            caisson2 = Rectangle(height=1.5, width=1, color=BLUE, fill_opacity=0.5)
            caisson2.move_to(wheel.point_at_angle(225 * DEGREES))
            
            scene_class.play(Create(wheel), Create(axle))
            scene_class.play(Create(caisson1), Create(caisson2))
            scene_class.wait(1)
            
            # Rotate the wheel
            wheel_group = VGroup(wheel, caisson1, caisson2, axle)
            scene_class.play(Rotate(wheel_group, angle=180 * DEGREES, run_time=4))
            scene_class.wait(2)
            # Create versel_engine.py
import json
from api.deepseek_integration import DeepSeekAI
from animators.manim_animator import ManimAnimator

class VerselEngine:
    def __init__(self, deepseek_api_key):
        self.ai = DeepSeekAI(deepseek_api_key)
        self.animator = ManimAnimator()
        self.animation_cache = {}
    
    def process_prompt(self, user_prompt):
        """Main function: Transform prompt → logic → animation"""
        
        print(f"🎯 Processing: {user_prompt}")
        
        # Step 1: Generate educational logic
        logic_response = self.ai.generate_stepwise_logic(user_prompt)
        stepwise_logic = self._parse_logic_response(logic_response)
        
        print(f"✅ AI Analysis Complete: {stepwise_logic['domain']}")
        
        # Step 2: Create animation based on logic
        video_path = self._generate_animation(stepwise_logic, user_prompt)
        
        return {
            "success": True,
            "stepwiseLogic": stepwise_logic,
            "videoPath": video_path,
            "message": "Educational video generated successfully!"
        }
    
    def _generate_animation(self, logic, prompt):
        """Generate the actual animation video"""
        domain = logic.get('domain', 'general')
        
        # Create dynamic animation class
        animation_class = type(
            f"VerselAnimation",
            (Scene,),
            {"construct": lambda self: self._create_animation(self, logic)}
        )
        
        # Render the animation
        video_path = f"media/videos/versel_{hash(prompt)}.mp4"
        
        return video_path
    // pages/index.js - Main VERSEL interface
import { useState } from 'react'

export default function VerselInterface() {
  const [prompt, setPrompt] = useState('')
  const [isGenerating, setIsGenerating] = useState(false)
  const [result, setResult] = useState(null)

  const generateVideo = async () => {
    setIsGenerating(true)
    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      })
      const data = await response.json()
      setResult(data)
    } catch (error) {
      console.error('Generation failed:', error)
    } finally {
      setIsGenerating(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-2">VERSEL</h1>
        <p className="text-gray-400 mb-8">AI-Powered STEM Video Generator</p>
        
        {/* Prompt Input */}
        <div className="mb-6">
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Hie Versel :) Can you show me how the Falkirk Wheel works?"
            className="w-full p-4 bg-gray-800 rounded-lg border border-gray-700 focus:border-blue-500 focus:outline-none"
          />
        </div>
        
        <button
          onClick={generateVideo}
          disabled={isGenerating}
          className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg font-semibold disabled:opacity-50"
        >
          {isGenerating ? 'Generating...' : 'Create Educational Video'}
        </button>

        {/* Results Display */}
        {result && (
          <div className="mt-8 p-6 bg-gray-800 rounded-lg">
            <h3 className="text-xl font-semibold mb-4">🎯 AI Analysis Complete</h3>
            <div className="grid grid-cols-2 gap-4 mb-4">
              <div className="bg-green-500/10 p-3 rounded">
                <span className="text-green-400">✅ Domain:</span> {result.stepwiseLogic?.domain}
              </div>
              <div className="bg-blue-500/10 p-3 rounded">
                <span className="text-blue-400">⚡ Engine:</span> {result.stepwiseLogic?.animationEngine}
              </div>
            </div>
            
            {/* Stepwise Logic */}
            <div className="mb-4">
              <h4 className="font-semibold mb-2">Step-by-Step Logic:</h4>
              <ol className="list-decimal list-inside space-y-2">
                {result.stepwiseLogic?.steps?.map((step, index) => (
                  <li key={index} className="text-gray-300">{step}</li>
                ))}
              </ol>
            </div>

            {/* Video Player */}
            {result.videoPath && (
              <div className="mt-6">
                <video controls autoPlay className="w-full rounded-lg">
                  <source src={result.videoPath} type="video/mp4" />
                </video>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}
